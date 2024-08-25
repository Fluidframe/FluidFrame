import json, inspect, html as HTML
from abc import ABC, abstractmethod
from fluidframe.utils import get_lib_path
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from fluidframe.core.dependency import requires
from fluidframe.utilities.helper import generate_id
from fluidframe.core.wrappers import html_render_wrap
from typing import Optional, Callable, Dict, List, Any
from starlette.middleware.sessions import SessionMiddleware
from fluidframe.config import PUBLIC_DIR, HOT_RELOAD_SCRIPT
from fluidframe.utilities.tailwind_utils import tailwind_build
from starlette.websockets import WebSocketDisconnect, WebSocket
from fluidframe.core import html, body, meta, script, div, head, title, div



class State:
    def __init__(self) -> None:
        self.id:                    str
        self.type:                  str = self.__class__.__name__.lower()
        self.state:                 Dict[str: Any] = {}
        self._parent_:              Optional['Component'] = None
        self.f_attributes:          Dict[str, Any] = {}
        self._event_registry_:      Dict[str, Callable] = {}
        self._state_bind_registry_: Dict[str, List[str]] = {}
        
    def use_state(self, state: Optional[dict]=None, exclude: List[str]|str=None, include: List[str]|str=None) -> None:
        exclude_set = set([exclude] if isinstance(exclude, str) else exclude or [])
        include_set = set([include] if isinstance(include, str) else include or [])

        init_method = self.__class__.__init__
        source_lines = inspect.getsource(init_method).split('\n')
            
        self.state = {}
        serializable_types = (str, dict, list, float, int)

        for line in source_lines:
            line = line.strip()
            if line.startswith('self.'):
                attr = line.split('=')[0].split('.')[1].strip()
                if (not include_set or attr in include_set) and attr not in exclude_set and hasattr(self, attr):
                    value = getattr(self, attr)
                    if isinstance(value, serializable_types):
                        self.state[attr] = value

        if state:
            self.state.update({k: v for k, v in state.items() if k not in exclude_set})         
            
    def bind_state(self, route_path: str, components: 'Component'|List['Component']) -> str:
        bind_state = {}
        
        if isinstance(components, Component):
            components = [components]
            
        if route_path not in self._state_bind_registry_:
            self._state_bind_registry_[route_path] = []
            
        for comp in components:
            idx=0
            while comp.type in self._state_bind_registry_[route_path]:
                idx+=1
            alias = f"{comp.type}{idx}" if idx > 0 else comp.type
            self._state_bind_registry_[route_path].append(alias)
            bind_state[comp.id] = {'alias': alias, 'keys': list(comp.state.keys())}
        return HTML.escape(json.dumps(bind_state))
    
    def set_state(self) -> str:
        return HTML.escape(json.dumps(self.state))
        
    def on_event(self, event: str, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind_state: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        # NOTE: Currently only supports a single event to be binded to a component
        
        route_path = f"/{self.id}/{event}"
        self.f_attributes['hx-swap'] = swap
        self.f_attributes['hx-trigger'] = event
        self.f_attributes['hx-get'] = route_path
        if use_cache:
            self.f_attributes['hx-trigger'] += " once"
        if use_transition:
            self.f_attributes['hx-swap'] += " transition:true"
        if bind_state:
            self.f_attributes['bind-state'] = self.bind_state(route_path, bind_state)
        if self.state:
            self.f_attributes['state'] = HTML.escape(json.dumps(self.state))
        if target:
            if isinstance(target, str):
                target_ids = f"#{target}"
            elif isinstance(target, Component):
                target_ids = f"#{target.id}" 
            elif isinstance(target, list):
                if isinstance(target, str): 
                    target_ids = f"{', '.join([f'#{t}' for t in target])}"
                else: 
                    target_ids =f"{', '.join([f'#{t.id}' for t in target])}"
            self.f_attributes['hx-target'] = target_ids
        
        def decorator(func: Callable):
            original_render = self.render
            def wrapped_render(*args, **kwargs) -> str:
                rendered_content = original_render(*args, **kwargs)
                rendered_content = rendered_content.replace(f'id="{self.id}"', "")
                htmx_div = div(rendered_content, id=self.id, cls="block w-max p-0 m-0", **self.f_attributes)
                return htmx_div
            self.render = wrapped_render

            # Register the route
            self._event_registry_[route_path] = func
            if self._parent_:
                self._parent_._event_registry_.update(self._event_registry_)

            return func
        return decorator
    
    def render(self) -> str:
        pass
    


class Component(State, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.id:                 str = generate_id(self.type)
        self.root:               Optional[FluidFrame] = None
        self.styles:             List[str] = []
        self.scripts:            List[str] = []
        self.children:           List[Component|str] = []
    
    def child(self, component: 'Component') -> 'Component':
        if isinstance(component, Component):
            component.root = self.root
            component._parent_ = self
            self._event_registry_.update(component._event_registry_)
        self.children.append(component)
        return component
    
    def add_children(self, *components: 'Component') -> 'Component':
        for component in components:
            self.child(component)
        return self
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    def click(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind_state: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        return self.on_event("click", swap, target, bind_state, use_transition, use_cache) 
    
    def mouseenter(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind_state: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        return self.on_event("mouseenter", swap, target, bind_state, use_transition, use_cache) 
    
    def mouseexit(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind_state: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        return self.on_event("mouseexit", swap, target, bind_state, use_transition, use_cache) 
 
    

class FluidFrame(Starlette):
    def __init__(self, dev_mode: bool = False) -> None:
        super().__init__()
        self.id:                 str = "root"
        self.dev_mode:           bool = dev_mode
        self.children:           List[Component] = []
        self._event_registry_:   Dict[str, Callable] = {}
    
    def child(self, component: 'Component') -> 'Component':
        if isinstance(component, Component):
            component.root = self
            component._parent_ = self
            self._event_registry_.update(component._event_registry_)
        self.children.append(component)
        return component
    
    def add_fluidroute(self, path: str, handler: Callable, **kwargs) -> None:
        wrapped_endpoint = html_render_wrap(handler)
        self.add_route(path, wrapped_endpoint, **kwargs)
        
    async def hot_reload_socket(self, ws: WebSocket):
        await ws.accept()
        try:
            while True:
                msg = await ws.receive_text()
                if msg=="ping":
                    await ws.send_text("pong")
        except WebSocketDisconnect:
            print('Client connection closed')
            
    def add_children(self, *components: 'Component') -> 'Component':
        for component in components:
            self.child(component)
        return self
    
    def render(self) -> str:
        return ''.join(["<!DOCTYPE html>",
            html(lang="eng",
                i=[
                    head(
                        title("Fluidframe App"),
                        meta(charset="UTF-8"),
                        script(src="https://cdn.tailwindcss.com"),
                        script(src=f"{PUBLIC_DIR}/scripts/state_manager.js"),
                        script(src=f"{PUBLIC_DIR}/scripts/dependency_manager.js"),
                        script(src="https://cdnjs.cloudflare.com/ajax/libs/htmx/2.0.2/htmx.min.js", async_=True),
                        requires(HOT_RELOAD_SCRIPT) if self.dev_mode else "",
                    ),
                    body(
                        div(
                            id=self.id,
                            i=[child.render() if isinstance(child, Component) else child for child in self.children],
                        ),
                        cls="relative dark:bg-gray-800 bg-white text-sm text-gray-900 dark: text-white"
                    )
                ]
            )
        ])
        
    def build(self):
        self._event_registry_["/"] = self.render
        for path, handler in self._event_registry_.items():
            self.add_fluidroute(path, handler)
        
        if self.dev_mode:
            self.add_websocket_route("/live-reload", self.hot_reload_socket)
        else:
            tailwind_build()
        # self.add_middleware(SessionMiddleware, secret_key='your-secret-key')
        self.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=get_lib_path("public")))
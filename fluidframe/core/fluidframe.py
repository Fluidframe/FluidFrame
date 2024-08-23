from abc import ABC, abstractmethod
from fluidframe.utils import get_lib_path
from starlette.responses import JSONResponse
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from fluidframe.core.dependency import requires
from typing import Optional, Callable, Dict, List
from fluidframe.utilities.helper import generate_id
from fluidframe.core.wrappers import html_render_wrap
from starlette.middleware.sessions import SessionMiddleware
from fluidframe.config import PUBLIC_DIR, HOT_RELOAD_SCRIPT
from starlette.websockets import WebSocketDisconnect, WebSocket
from fluidframe.core import html, body, meta, script, link, div, head, title, div


class Component(ABC):
    def __init__(self) -> None:
        self.styles = []
        self.scripts = []
        self.children = []
        self.root: Optional[FluidFrame] = None
        self.htmx_attributes: Dict[str, str] = {}
        self.type = self.__class__.__name__.lower()
        self.__parent__: Optional['Component'] = None
        self.id = generate_id(self.type)
    
    def child(self, component: 'Component') -> 'Component':
        if isinstance(component, Component):
            component.__parent__=self
            component.root = self.root
        self.children.append(component)
        return component
    
    @abstractmethod
    def render(self) -> str:
        pass
    
    def on_event(self, trigger: str, target: 'Component'|List['Component'], action: str, transition: bool = True, cache: bool = False) -> Callable:
        
        trigger = f"{trigger} once" if cache else trigger
        action = f"{action} transition:true" if transition else action
        target_ids = f"#{target.id}" if isinstance(target, Component) else f"{', '.join([f'#{t.id}' for t in target])}"
        
        def decorator(func: Callable):
            route_path = f"/{self.id}/{trigger}"
            # Add HTMX attributes to the component
            self.htmx_attributes.update({
                "hx-swap": action,
                "hx-get": route_path,
                "hx-trigger": trigger,
                "hx-target": target_ids
            })

            # Wrap the original render method to include HTMX attributes
            original_render = self.render
            def wrapped_render(*args, **kwargs) -> str:
                rendered_content = original_render(*args, **kwargs)
                rendered_content = rendered_content.replace(f'id="{self.id}"', "")
                htmx_div = div(rendered_content, id=self.id, cls="block w-max p-0 m-0", **self.htmx_attributes)
                return htmx_div
            self.render = wrapped_render

            # Register the route
            self.root.add_event_route(route_path, func)
            return func
        return decorator
    

class FluidFrame(Starlette):
    def __init__(self, reload: bool = False) -> None:
        super().__init__()
        self.id = "root"
        self.reload = reload
        self.children: List[Component] = []
        self.add_fluidroute("/", self.render)
        self.add_websocket_route("/live-reload", self.hot_reload_socket)
        self.add_middleware(SessionMiddleware, secret_key='your-secret-key')
        self.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=str(get_lib_path() / "public")))
    
    def child(self, component: 'Component') -> 'Component':
        if isinstance(component, Component):
            component.root = self
            component.__parent__=self
        self.children.append(component)
        return component
    
    def add_fluidroute(self, path: str, endpoint: Callable, **kwargs) -> None:
        wrapped_endpoint = html_render_wrap(endpoint)
        self.add_route(path, wrapped_endpoint, **kwargs)
        
    async def hot_reload_socket(self, ws: WebSocket):
        await ws.accept()
        try:
            while True:
                await ws.receive_text()
                await ws.send_text("pong")
        except WebSocketDisconnect:
            print('Client connection closed')
    
    def add_event_route(self, path: str, handler: Callable):
        self.add_fluidroute(path, handler)
    
    def render(self) -> str:
        return ''.join(["<!DOCTYPE html>",
            html(lang="eng",
                i=[
                    head(
                        title("Fluidframe App"),
                        meta(charset="UTF-8"),
                        script(src="https://cdn.tailwindcss.com"),
                        script(src=f"{PUBLIC_DIR}/scripts/dependency_manager.js"),
                        script(src="https://cdnjs.cloudflare.com/ajax/libs/htmx/2.0.2/htmx.min.js"),
                        requires(HOT_RELOAD_SCRIPT) if self.reload else "",
                    ),
                    body(
                        div(
                            id=self.id,
                            i=[child.render() if isinstance(child, Component) else child for child in self.children]
                        ),
                        cls="relative dark:bg-gray-800 bg-white text-sm text-gray-900 dark: text-white"
                    )
                ]
            )
        ])
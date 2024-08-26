import inspect, json
from typing import Callable
import json, inspect, html as HTML
from abc import ABC, abstractmethod
from starlette.requests import Request
from fluidframe.core.state import State
from fluidframe.utils import get_lib_path
from starlette.responses import HTMLResponse
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from fluidframe.core.dependency import requires
from fluidframe.utilities.helper import generate_id
from typing import Optional, Callable, Dict, List, Any
from starlette.middleware.sessions import SessionMiddleware
from fluidframe.config import PUBLIC_DIR, HOT_RELOAD_SCRIPT
from fluidframe.utilities.tailwind_utils import tailwind_build
from starlette.websockets import WebSocketDisconnect, WebSocket
from fluidframe.core import html, body, meta, script, div, head, title, div



class StateRegistry:
    """
    A base class for managing component state and event handling.

    This class provides functionality for state management, event binding, and HTMX integration.
    """
    def __init__(self) -> None:
        """Initialize a StateRegistry instance."""
        self.id:                    str
        self.type:                  str = self.__class__.__name__.lower()
        self.state:                 Dict[str: Any] = {}
        self._parent_:              Optional['Component'] = None
        self.f_attributes:          Dict[str, Any] = {}
        self._event_registry_:      Dict[str, Callable] = {}
        self._state_bind_registry_: Dict[str, List[str]] = {}
        
    def use_state(self, state: Optional[dict]=None, exclude: List[str]|str=None, include: List[str]|str=None) -> None:
        """
        Configure the state for the component.

        Args:
            `state` (Optional[dict]): Additional state to include.
            `exclude` (List[str]|str): Attributes to exclude from the state.
            `include` (List[str]|str): Attributes to specifically include in the state.

        This method automatically includes serializable attributes from the component's __init__ method.
        """
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
        """
        Bind state to components for a specific event route.

        Args:
            `route_path` (str): The route path to bind the state to.
            `components` (Component|List[Component]): The component(s) to bind the state to.

        Returns:
            str: JSON-encoded string of the bound state.
        """
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
    
    def add_state(self) -> str:
        """
        Get the current state as a JSON-encoded string to be added as `state` attribute value.

        Returns:
            str: HTML-escaped JSON string of the current state.
        """
        return HTML.escape(json.dumps(self.state))
        
    def on_event(self, event: str, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        """
        Decorator for handling component events.

        Args:
            `event` (str): The event type (e.g., "click").
            `swap` (str): The HTMX swap method.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
            `bind` (Optional[Component|List[Component]]): Component(s) to bind state to.
            `use_transition` (bool): Whether to use HTMX transitions.
            `use_cache` (bool): Whether to cache the result of the event.

        Returns:
            Callable: A decorator for the event handler function.
        """
        # NOTE: Currently only supports a single event to be binded to a component
        
        route_path = f"/{self.id}/{event}"
        self.f_attributes['hx-swap'] = swap
        self.f_attributes['hx-trigger'] = event
        self.f_attributes['hx-get'] = route_path
        if use_cache:
            self.f_attributes['hx-trigger'] += " once"
        if use_transition:
            self.f_attributes['hx-swap'] += " transition:true"
        if bind:
            self.f_attributes['bind-state'] = self.bind_state(route_path, bind)
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
        """
        Render the component.

        This method should be overridden by subclasses.

        Returns:
            str: The rendered HTML string.
        """
        pass
    


class Component(StateRegistry, ABC):
    """
    An abstract base class for creating reusable UI components.

    This class serves as the foundation for building interactive UI elements in the FluidFrame framework.
    It provides mechanisms for state management, event handling, and composition of UI elements.

    ### Key features:
    
    1. State Management: Components can manage their own state using the `use_state` method.
    2. Event Handling: The `on_event` decorator allows binding of various events to component methods.
    3. Composition: Components can be nested using the `child` and `add_children` methods.

    ### State Management:
    
    To manage state within a component, use the `use_state` method in the component's `__init__` method.
    This allows you to specify which attributes should be included in the component's state.

        #### Important: When `use_state` is called, you must include `self.add_state()` in the component's `render` method
    to properly bind the state to the component's HTML output.
    
    ### Event Handling:
    
    The `on_event` decorator (and its aliases like `click`, `mouseenter`, etc.) allows you to bind
    events to component methods. This integration with HTMX enables dynamic updates without full page reloads.

    Examples:
    
    ```python 
        from fluidframe.core import p, button, div, h2
        from fluidframe.core import FluidFrame, Component, State
    
        ###########################
        # Component without state #
        ###########################
        class SimpleButton(Component):
            def __init__(self, label: str):
                super().__init__()
                self.label = label

            def render(self) -> str:
                return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 py-2 px-5")

        ###########################
        # Component with children #
        ###########################
        class Card(Component):
            def __init__(self, title: str, children: List[Component] = []):
                super().__init__()
                self.title = title
                self.children = children

            def render(self) -> str:
                children_html = ''.join([child.render() for child in self.children])
                return div(children_html, id=self.id, cls="max-w-md mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5")
                
        # Usage
        button1 = SimpleButton("Button 1")
        button2 = SimpleButton("Button 2")
        card = Card("My Card", [button1, button2])

        ########################
        # Component with state #
        ########################
        class Counter(Component):
            def __init__(self, initial_count: int = 0):
                super().__init__()
                self.count = initial_count
                self.use_state(include='count')

            def render(self) -> str:
                return div(f"Count: {self.count}", id=self.id, state=self.add_state())'

        ###########################################
        # Component with state and event handling #
        ###########################################
        class Button(Component):
            def __init__(self, label: str) -> None:
                super().__init__()
                self.label = label

            def render(self) -> str:
                return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg ")

        class Header(Component):
            def __init__(self, body: str) -> None:
                super().__init__()
                self.count = 0
                self.body = body
                self.text_id = f"{self.id}-text"
                self.use_state(include='count')
                
            def render(self) -> str:
                return div(
                    h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                    id=self.id, cls="relative", state=self.add_state()
                )

        # Creating instances
        app = FluidFrame()
        header = Header("The count is 0")
        increment_btn = Button("Increment")
        decrement_btn = Button("Decrement")

        # Binding click events
        @increment_btn.click(swap="textContent", target=header.text_id, bind_state=header)
        def increment(state: State) -> str:
            st = state.get_state()
            state.set_state('count', st['count']+1)
            return f"The count is {state.get('count')}"

        @decrement_btn.click(swap="textContent", target=header.text_id, bind_state=header)
        def decrement(state: State) -> str:
            st = state.get_state()
            state.set_state('count', st['count']-1)
            return f"The count is {state.get('count')}"
            
        # The `click` decorator is used to bind click events to the increment and decrement buttons.
        # The `swap` parameter specifies that the text content of the target should be updated.
        # The `target` parameter specifies which element should be updated (the header's text).
        # The `bind_state` parameter binds the header's state to the event, allowing it to be updated.
        # The event handler functions (`increment` and `decrement`) receive a `State` object, which they use to get the current state and set the new state.
        # The return value of the event handler is used to update the target element's content.

        # This pattern allows for creating interactive components where user actions (like button clicks) can trigger server-side logic and update the UI dynamically, all without a full page reload.
        
        # The order determines the alignment
        app.add_children(
            increment_btn, 
            header, 
            decrement_btn
        )
        
        app.build()
        if __name__ == '__main__':
            import uvicorn
            uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)
    ```
    """
    def __init__(self) -> None:
        """Initialize a Component instance."""
        super().__init__()
        self.id:                 str = generate_id(self.type)
        self.root:               Optional[FluidFrame] = None
        self.styles:             List[str] = []
        self.scripts:            List[str] = []
        self.children:           List[Component|str] = []
    
    def child(self, component: 'Component') -> 'Component':
        """
        Add a child component to this component.

        Args:
            `component` (Component): The child component to add.

        Returns:
            Component: The added child component.
        """
        if isinstance(component, Component):
            component.root = self.root
            component._parent_ = self
            self._event_registry_.update(component._event_registry_)
        self.children.append(component)
        return component
    
    def add_children(self, *components: 'Component') -> 'Component':
        """
        Add multiple child components to this component.

        Args:
            `*components` (Component|str): Variable number of child components or strings to add.

        Returns:
            Component: The current component instance.
        """
        for component in components:
            self.child(component)
        return self
    
    @abstractmethod
    def render(self) -> str:
        """
        Render the component.

        This method must be implemented by subclasses.

        Returns:
            str: The rendered HTML string.
        """
        pass
    
    def click(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        """
        Convenience method for binding `click` event to the component.

        Args:
            `swap` (str): The HTMX swap method.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
            `bind` (Optional[Component|List[Component]]): Component(s) to bind state to.
            `use_transition` (bool): Whether to use HTMX transitions.
            `use_cache` (bool): Whether to cache the result of the event.

        Returns:
            Callable: A decorator for the click event handler function.
        """
        return self.on_event("click", swap, target, bind, use_transition, use_cache) 
    
    def mouseenter(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        """
        Convenience method for binding `mouseenter` event to the component.

        Args:
            `swap` (str): The HTMX swap method.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
            `bind` (Optional[Component|List[Component]]): Component(s) to bind state to.
            `use_transition` (bool): Whether to use HTMX transitions.
            `use_cache` (bool): Whether to cache the result of the event.

        Returns:
            Callable: A decorator for the mouseenter event handler function.
        """
        return self.on_event("mouseenter", swap, target, bind, use_transition, use_cache) 
    
    def mouseexit(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = True, use_cache: bool = False) -> Callable:
        """
        Convenience method for binding `mouseexit` event to the component.

        Args:
            `swap` (str): The HTMX swap method.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
            `bind` (Optional[Component|List[Component]]): Component(s) to bind state to.
            `use_transition` (bool): Whether to use HTMX transitions.
            `use_cache` (bool): Whether to cache the result of the event.

        Returns:
            Callable: A decorator for the mouseexit event handler function.
        """
        return self.on_event("mouseexit", swap, target, bind, use_transition, use_cache) 
 
    

class FluidFrame(Starlette):
    """
    The main application class for the FluidFrame framework.

    This class extends Starlette to provide FluidFrame-specific functionality.
    """
    def __init__(self, dev_mode: bool = False) -> None:
        """
        Initialize a FluidFrame application.

        Args:
            `dev_mode` (bool): Whether to run the application in development mode.
        """
        super().__init__()
        self.id:                 str = "root"
        self.dev_mode:           bool = dev_mode
        self.children:           List[Component] = []
        self._event_registry_:   Dict[str, Callable] = {}
    
    def child(self, component: 'Component') -> 'Component':
        """
        Add a child component to the application.

        Args:
            `component` (Component|str): The child component to add.

        Returns:
            Component: The added child component.
        """
        if isinstance(component, Component):
            component.root = self
            component._parent_ = self
            self._event_registry_.update(component._event_registry_)
        self.children.append(component)
        return component
    
    def add_fluidroute(self, path: str, handler: Callable, **kwargs) -> None:
        """
        Add a route to the application with FluidFrame-specific handling.

        Args:
            `path` (str): The URL path for the route.
            `handler` (Callable): The function to handle requests to this route.
            `**kwargs`: Additional arguments to pass to Starlette's add_route method.
        """
        wrapped_endpoint = html_render_wrap(handler)
        self.add_route(path, wrapped_endpoint, **kwargs)
        
    async def hot_reload_socket(self, ws: WebSocket):
        """
        WebSocket handler for hot reloading in development mode.

        Args:
            ws (WebSocket): The WebSocket connection.
        """
        await ws.accept()
        try:
            while True:
                msg = await ws.receive_text()
                if msg=="ping":
                    await ws.send_text("pong")
        except WebSocketDisconnect:
            print('Client connection closed')
            
    def add_children(self, *components: 'Component') -> 'Component':
        """
        Add multiple child components to the application.

        Args:
            `*components` (Component): Variable number of child components to add.

        Returns:
            Component: The current FluidFrame instance.
        """
        for component in components:
            self.child(component)
        return self
    
    def render(self) -> str:
        """
        Render the entire application.

        Returns:
            str: The rendered HTML string for the complete application.
        """
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
        """
        Build the application, setting up routes and middleware.

        This method should be called after all components and routes have been added.
        """
        self._event_registry_["/"] = self.render
        for path, handler in self._event_registry_.items():
            self.add_fluidroute(path, handler)
        
        if self.dev_mode:
            self.add_websocket_route("/live-reload", self.hot_reload_socket)
        else:
            tailwind_build()
        # self.add_middleware(SessionMiddleware, secret_key='your-secret-key')
        self.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=get_lib_path("public")))
        
        
        
def html_render_wrap(func: Callable) -> HTMLResponse:
    async def wrapped_func(request: Request) -> HTMLResponse:
        sig = inspect.signature(func)
        kwargs = {}
        state = State(request)
        if sig.parameters:
            for name, param in sig.parameters.items():
                if name == 'request' or (param.annotation is Request):
                    kwargs[name] = request
                elif name == 'state' or (param.annotation is State):
                    kwargs[name]=state
                elif param.default is param.empty:
                    raise ValueError(f"Required parameter {name} is not a valid parameter either specify `request`, `state` or both as parameters")
            result = await func(**kwargs) if inspect.iscoroutinefunction(func) else func(**kwargs)
        else:
            result = await func() if inspect.iscoroutinefunction(func) else func()
        response = []
        if isinstance(result, tuple):
            for r in result:
                if isinstance(r, str):
                    response.append(r)
                elif isinstance(r, Component):
                    response.append(r.render())
        elif isinstance(result, str):
            response.append(result)
        elif isinstance(result, Component):
            response.append(result.render())
        response = HTMLResponse(''.join(response))
        modifier = state.get_response_modifier()
        if modifier:
            response.headers.update(state.get_response_modifier())
        return response

    return wrapped_func
import inspect
from typing import Callable
from starlette.requests import Request
from fluidframe.core.state import State
from typing import Callable, Dict, List
from fluidframe.config import get_lib_path
from starlette.responses import HTMLResponse
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from fluidframe.core.component import Component
from fluidframe.core.dependency import requires
from fluidframe.config import PUBLIC_DIR, HOT_RELOAD_SCRIPT
from fluidframe.utilities.tailwind_utils import tailwind_build
from starlette.websockets import WebSocketDisconnect, WebSocket
from fluidframe.core import html, body, meta, script, div, head, title, div



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
        self.id:              str = "root"
        self.dev_mode:        bool = dev_mode
        self.children:        List[Component] = []
        self._route_registry: Dict[str, Callable] = {}
    
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
            component._parent = self
            component._state_event_wrap_()
            self._route_registry.update(component._event_registry)
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
                        requires(HOT_RELOAD_SCRIPT) if self.dev_mode else ""
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
        self._route_registry["/"] = self.render
        for path, handler in self._route_registry.items():
            self.add_fluidroute(path, handler)
        
        if self.dev_mode:
            self.add_websocket_route("/live-reload", self.hot_reload_socket)
        else:
            tailwind_build()
        self.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=get_lib_path("public")))
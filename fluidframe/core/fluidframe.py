import inspect, os
from typing import Callable
from starlette.requests import Request
from fluidframe.core.state import State
from typing import Callable, Dict, List
from fluidframe.config import PUBLIC_DIR
from fluidframe.config import get_lib_path
from starlette.responses import HTMLResponse
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from fluidframe.core.component import Component
from fluidframe.core.dependency import requires
from fluidframe.public import js_bundle as fluidframe_bundle
from fluidframe.utilities.package_manager import url_for_public
from starlette.websockets import WebSocketDisconnect, WebSocket
from fluidframe.utilities.package_manager import get_node_manager
from fluidframe.core import html, body, meta, script, div, head, title, div, link



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



class Page(Component):
    
    def __init__(self, endpoint: str, title: str|None = None) -> None:
        """
        Initialize the page.

        Args:
            endpoint (str): The endpoint of the page.
            title (str|None): The title of the page. Defaults to "Fluidframe".
        """
        super().__init__()
        self.id = endpoint
        self.title = title or "Fluidframe"
    
    def render(self) -> str:
        """
        Render the page.

        This method renders the HTML page.

        Returns:
            str: The rendered HTML string.
        """
        return ''.join(["<!DOCTYPE html>",
            html(lang="eng",
                i=[
                    head(
                        title(self.title),
                        meta(charset="UTF-8"),
                        link(href="fluidbuild/dist/output.css", rel="stylesheet"),
                        script(src=url_for_public(fluidframe_bundle.scripts.fluidframe_bundle_js)),
                        script(src=url_for_public(fluidframe_bundle.scripts.htmx_bundle_js), async_=True),
                        requires(url_for_public(fluidframe_bundle.scripts.hot_reload_js))
                    ),
                    body(
                        div(
                            id=self.id,
                            i=self.render_children(),
                        ),
                        cls="relative dark:bg-gray-800 bg-white text-sm text-gray-900 dark: text-white"
                    )
                ]
            )
        ])

    

class FluidFrame(Starlette):

    def __init__(self, dev_mode: bool = False) -> None:
        """
        Initialize a FluidFrame instance.

        Args:
            dev_mode (bool): Whether the development mode is enabled. Defaults to False.

        Attributes:
            id (str): The id of the root component.
            pages (List[Page]): A list of pages.
            dev_mode (bool): Whether the development mode is enabled.
            children (List[Component]): A list of children components.
            entry_page (Page): The entry page.
            _route_registry (Dict[str, Callable]): A dictionary of route registry.
            _fluidbuild_dir (str): The directory of fluidbuild.
        """
        super().__init__() 
        self.id:              str = "root"
        self.pages:           List[Page] = []
        self.dev_mode:        bool = dev_mode
        self.children:        List[Component] = []
        self.entry_page:      Page|None = None
        self._route_registry: Dict[str, Callable] = {}
        self._fluidbuild_dir: str|None = None
    
    def render(self) -> str:
        """
        Render the entry page of the FluidFrame instance.

        This method simply delegates to the render method of the entry page
        of the FluidFrame instance.

        Returns:
            str: The rendered HTML string of the entry page.
        """
        
        return self.entry_page.render()
    
    def mount_fluidbuild(self, fluidframe_dir: str) -> None:
        """
        Mount the fluidbuild directory to the FluidFrame instance.

        This method sets the _fluidbuild_dir attribute of the FluidFrame instance to the given fluidframe_dir.
        """
        self._fluidbuild_dir = fluidframe_dir
        
    def add_fluidroute(self, path: str, handler: Callable, **kwargs) -> None:
        """
        Add a route to the application with automatic wrapping of the handler to return an HTML response.

        This method is similar to `add_route`, but it wraps the handler with
        `html_render_wrap` to ensure that the handler returns an HTML response.

        Parameters
        ----------
        path : str
            The path for the route.
        handler : Callable
            The handler for the route.
        **kwargs
            Additional keyword arguments to be passed to the handler.

        Returns
        -------
        None
        """
        wrapped_endpoint = html_render_wrap(handler)
        self.add_route(path, wrapped_endpoint, **kwargs)
    
    def add_page(self, *pages: 'Page') -> 'FluidFrame':
        """
        Add one or more pages to the fluidframe application.

        Pages can be `Page` instances or subclasses of `Component`. The
        pages will be added to the application's route registry and will be
        accessible via HTTP requests to the root of the application.

        Args: 
            *pages: One or more `Page` instances or subclasses of `Component`
            
        Returns:
            The fluidframe application
        """
        for page in pages:
            self.child(page)
        return self
        
    def set_entry_page(self, page: Page) -> 'FluidFrame':
        """
        Set the entry page of the fluidframe application.

        The entry page is the page that will be rendered when the user visits
        the root of the application. This page should be a `Page` component.

        Args:
            page: The page to set as the entry page.

        Returns:
            The fluidframe application
        """
        page.id = "/"
        self.child(page)
        self.entry_page = page
        return self
    
    def child(self, component: 'Component') -> 'Component':
        """
        Mount a component to the fluidframe application.

        Args:
            component: The component to be mounted.

        Returns:
            The mounted component.
        """
        if isinstance(component, Component):
            component.root = self
            component._parent = self
            component._state_event_wrap_()
            self._route_registry.update(component._event_registry)
        self.children.append(component)
        return component
        
    async def hot_reload_socket(self, ws: WebSocket):
        """
        Handle hot reload WebSockets connection.

        This method is registered as an ASGI endpoint and is called whenever a WebSocket
        connection is established. It continuously listens for incoming messages on the
        connection and responds to "ping" messages with a "pong" message. If the connection
        is closed, it prints a message to the console.

        Parameters
        ----------
        ws : WebSocket
            The WebSocket connection to handle.
        """
        await ws.accept()
        try:
            while True:
                msg = await ws.receive_text()
                if msg=="ping":
                    await ws.send_text("pong")
        except WebSocketDisconnect:
            print('Client connection closed')
        
    def build(self):
        """
        Builds the FluidFrame application.

        This method registers all components as routes, and mounts the fluidbuild
        directory (if specified) and the public directory at the root URL.

        It also builds the Tailwind CSS stylesheets if not in development mode.

        :return: None
        """
        self._route_registry["/"] = self.render
        
        for path, handler in self._route_registry.items():
            self.add_fluidroute(path, handler)
        
        if self.dev_mode:
            self.add_websocket_route("/live-reload", self.hot_reload_socket)
        else:
            get_node_manager().tailwind_build()
        
        if self._fluidbuild_dir is None:
            print("Please use `app.mount_fluidbuild` method to mount your fluidbuild folder")
        else:
            self.mount("/fluidbuild", StaticFiles(directory=self._fluidbuild_dir))
        
        self.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=get_lib_path("public")))
        
        # os.chdir('../src')
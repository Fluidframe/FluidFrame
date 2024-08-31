import json, inspect
from typing import Callable
from abc import ABC, abstractmethod
from html import escape as escape_html
from typing import Optional, Callable, Dict, List, Any, TYPE_CHECKING
from fluidframe.utilities.helper import generate_id, update_outer_div


if TYPE_CHECKING:
    from fluidframe.core.fluidframe import FluidFrame

class StateRegistry:
    """
    A base class for managing component state and event handling.

    This class provides functionality for state management, event binding, and HTMX integration.
    """
    def __init__(self) -> None:
        """Initialize a StateRegistry instance."""
        self.id:                   str
        self.type:                 str = self.__class__.__name__.lower()
        self.state:                Dict[str: Any] = dict()
        self._parent:              Optional['Component'] = None
        self._f_attributes:         Dict[str, Any] = dict()
        self._event_registry:      Dict[str, Callable] = dict()
        self._hx_trigger_info:     Dict[str, Any] = dict()
        self._state_bind_registry: Dict[str, List[str]] = dict()
        
    def use_state(self, state: Optional[dict]=None, exclude_attributes: bool=True, exclude: List[str]|str=None, include: List[str]|str=None) -> None:
        """
        Configure the state for the component.

        Args:
            `state` (Optional[dict]): Additional state to include.
            `exclude_attributes` (bool): Whether to exclude internal attributes from the state.
            `exclude` (List[str]|str): Attributes to exclude from the state.
            `include` (List[str]|str): Attributes to specifically include in the state.

        This method automatically includes serializable attributes from the component's __init__ method.
        """
        exclude_set = set([exclude] if isinstance(exclude, str) else exclude or [])
        include_set = set([include] if isinstance(include, str) else include or [])

        if not exclude_attributes:
            init_method = self.__class__.__init__
            source_lines = inspect.getsource(init_method).split('\n')
        
            serializable_types = (str, dict, list, float, int)

            for line in source_lines:
                line = line.strip()
                if line.startswith('self.'):
                    attr = line.split('=')[0].split('.')[1].strip()
                    if (not include_set or attr in include_set) and attr not in exclude_set and hasattr(self, attr):
                        value = getattr(self, attr)
                        if isinstance(value, serializable_types):
                            self.state[attr] = value

        if isinstance(state, dict):
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
            
        if route_path not in self._state_bind_registry:
            self._state_bind_registry[route_path] = []
            
        for comp in components:
            idx=0
            while comp.type in self._state_bind_registry[route_path]:
                idx+=1
            alias = f"{comp.type}{idx}" if idx > 0 else comp.type
            self._state_bind_registry[route_path].append(alias)
            # bind_state[comp.id] = {'alias': alias, 'keys': list(comp.state.keys())}
            bind_state[comp.id] = {alias: list(comp.state.keys())}
        return escape_html(json.dumps(bind_state))
    
    def add_state(self) -> str:
        """
        Get the current state as a JSON-encoded string to be added as `state` attribute value.

        Returns:
            str: HTML-escaped JSON string of the current state.
        """
        return escape_html(json.dumps(self.state))
        
    def on_event(self, event: str, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = False) -> Callable:
        """
        Decorator for handling component events.

        This method sets up HTMX-based event handling for a component. It configures the necessary attributes
        and routing for the specified event.

        Args:
            `event` (str): The event type to handle (e.g., "click", "mouseenter", "mouseleave").
            `swap` (str): The HTMX swap method. Determines how the response will be inserted into the DOM. Refer to the HTMX [documentation](https://htmx.org/attributes/hx-swap/#hx-swap) for more information.
                
                **Valid values are:**
                - "innerHTML": Replace the inner HTML of the target element (default).
                - "outerHTML": Replace the entire target element with the response.
                - "textContent": Replace the text content of the target element, without parsing the response as HTML.
                - "beforebegin": Insert the response before the target element.
                - "afterbegin": Insert the response before the first child of the target element.
                - "beforeend": Insert the response after the last child of the target element.
                - "afterend": Insert the response after the target element.
                - "delete": Delete the target element regardless of the response.
                - "none": Do not append content from response (out-of-band items will still be processed).
                
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
                Can be a single Component, a list of Components, a string ID, or a list of string IDs.
                If not specified, the current component is used as the target.
            
            `bind` (Optional[Component|List[Component]]): Component(s) whose state should be bound to this event.
                This allows for automatic state synchronization between components.
            
            `use_transition` (bool): Whether to use HTMX transitions for the event. Only applicable for 'click' events currently due to flickering on other events. [Refer](https://htmx.org/attributes/hx-swap/#modifiers)

        Returns:
            Callable: A decorator for the event handler function.

        Note:
            This method internally sets up the necessary HTMX attributes and routing for the specified event.
            It also handles the creation of target selectors and manages component state binding if specified.
        """
        
        target_ids = f"#{self.id}"
        route_path = f"/{self.id}/{event}"
        self._hx_trigger_info[event] = dict()
        
        if target is None:
            target = self

        if use_transition and event=='click':
            swap = f"{swap} transition:true"
            
        if self.state:
            self._f_attributes['state'] = self.add_state()
        
        if bind is None:
            bind = self
        self._f_attributes['bind-state'] = self.bind_state(route_path, bind)
            
        if isinstance(target, str):
            target_ids = f"#{target}"
        elif isinstance(target, Component):
            target_ids = f"#{target.id}" 
        elif isinstance(target, list):
            if isinstance(target, str): 
                target_ids = f"{', '.join([f'#{t}' for t in target])}"
            else: 
                target_ids =f"{', '.join([f'#{t.id}' for t in target])}"
            
        self._hx_trigger_info[event]['swap'] = swap
        self._hx_trigger_info[event]['method'] = 'GET'
        self._hx_trigger_info[event]['path'] = route_path
        self._hx_trigger_info[event]['target'] = target_ids
        
        self._f_attributes['hx-trigger-info'] = escape_html(json.dumps(self._hx_trigger_info))
        
        def decorator(func: Callable):
            """
            A decorator for event handlers that sets up the HTMX trigger
            information and registers the route.

            Args:
                func (Callable): The event handler function to be decorated.

            Returns:
                Callable: The decorated event handler function.
            """
            original_render = self.render
            def wrapped_render(*args, **kwargs) -> str:
                rendered_content = original_render(*args, **kwargs)
                rendered_content = update_outer_div(rendered_content, self._f_attributes)
                return rendered_content
            self.render = wrapped_render

            # Register the route
            self._event_registry[route_path] = func
            if self._parent:
                self._parent._event_registry.update(self._event_registry)

            return func
        return decorator
    
    def _state_event_wrap_(self) -> Callable:
        """
        Internal wrapper to add state to components when rendered.

        This method is used internally by FluidFrame to add the state to the component
        when it is rendered. It is not intended to be used directly by the user.

        If the component has state, it will be added to the component as an attribute
        before rendering. The state will be added as a JSON-encoded string.
        """
        original_render = self.render
        def wrapped_render(*args, **kwargs) -> str:
            rendered_content = original_render(*args, **kwargs)
            if self.state:
                self._f_attributes['state'] = self.add_state()
                rendered_content = update_outer_div(rendered_content, self._f_attributes)
                return rendered_content
            else:
                return rendered_content
        self.render = wrapped_render
    
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
            def __init__(self, label: str, state:dict|None=None):
                super().__init__()
                self.label = label
                if state:
                    self.use_state(state)

            def render(self) -> str:
                return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 py-2 px-5")

        ###########################
        # Component with children #
        ###########################
        class Card(Component):
            def __init__(self, title: str, children: List[Component]=None, state:dict|None=None):
                super().__init__()
                self.title = title
                if children is None:
                    children = []
                self.children = children
                if state:
                    self.use_state(state)

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
                return div(f"Count: {self.count}", id=self.id)'

        ###########################################
        # Component with state and event handling #
        ###########################################
        class Button(Component):
            def __init__(self, label: str, state:dict=None) -> None:
                super().__init__()
                self.label = label
                if state:
                    self.use_state(state)

            def render(self) -> str:
                return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")

        class Header(Component):
            def __init__(self, body: str, state:dict=None) -> None:
                super().__init__()
                self.body = body
                self.text_id = f"{self.id}-text"
                if state:
                    self.use_state(state)
                
            def render(self) -> str:
                return div(
                    h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                    id=self.id
                )

        # Creating instances
        app = FluidFrame()
        increment_btn = Button("Increment")
        decrement_btn = Button("Decrement")
        header = Header("The count is 0", {'count': 0})

        # Binding click events
        @increment_btn.click(swap="textContent", target=header.text_id, bind=header)
        def increment(state: State) -> str:
            count = state.get('count')
            count+=1
            state.set('count', count)
            return f"The count is {count}"

        @decrement_btn.click(swap="textContent", target=header.text_id, bind=header)
        def decrement(state: State) -> str:
            count = state.get('count')
            count-=1
            state.set('count', count)
            return f"The count is {count}"
            
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
        self.root:               Optional['FluidFrame'] = None
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
            component._parent = self
            component._state_event_wrap_()
            self._event_registry.update(component._event_registry)
        self.children.append(component)
        return component
    
    def __call__(self, *components: 'Component') -> 'Component':
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
    
    def render_children(self) -> str:
        return ''.join([child.render() if isinstance(child, Component) else child for child in self.children])
    
    @abstractmethod
    def render(self) -> str:
        """
        Render the component.

        This method must be implemented by subclasses.

        Returns:
            str: The rendered HTML string.
        """
        pass
    
    def click(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None, use_transition: bool = False) -> Callable:
        """
        Convenience method for binding a 'click' event to the component.

        This method is a shorthand for `on_event` with the event type set to "click".

        Args:
            `swap` (str): The HTMX swap method. See `on_event` for valid values and descriptions.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
                See `on_event` for details.
            `bind` (Optional[Component|List[Component]]): Component(s) whose state should be bound to this event.
            `use_transition` (bool): Whether to use HTMX transitions for the click event.

        Returns:
            Callable: A decorator for the click event handler function.

        Example:
            ```python
            @component.click(swap="innerHTML", target=header, use_transition=True)
            def handle_click():
                return "Button clicked!"
            ```
        """

        return self.on_event("click", swap, target, bind, use_transition) 
    
    def mouseenter(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None) -> Callable:
        """
        Convenience method for binding a 'mouseenter' event to the component.

        This method is a shorthand for `on_event` with the event type set to "mouseenter".

        Args:
            `swap` (str): The HTMX swap method. See `on_event` for valid values and descriptions.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
                See `on_event` for details.
            `bind` (Optional[Component|List[Component]]): Component(s) whose state should be bound to this event.

        Returns:
            Callable: A decorator for the mouseenter event handler function.

        Example:
            ```python
            @component.mouseenter(swap="beforeend", target=mycomponent)
            def handle_mouseenter():
                return "<p>Mouse entered the component!</p>"
            ```
        """
        return self.on_event("mouseenter", swap, target, bind, False) 
    
    def mouseleave(self, swap: str, target: Optional['Component'|List['Component']|str|List[str]]=None, bind: Optional['Component'|List['Component']]=None) -> Callable:
        """
        Convenience method for binding a 'mouseleave' event to the component.

        This method is a shorthand for `on_event` with the event type set to "mouseleave".

        Args:
            `swap` (str): The HTMX swap method. See `on_event` for valid values and descriptions.
            `target` (Optional[Component|List[Component]|str|List[str]]): The target(s) for the HTMX update.
                See `on_event` for details.
            `bind` (Optional[Component|List[Component]]): Component(s) whose state should be bound to this event.

        Returns:
            Callable: A decorator for the mouseleave event handler function.

        Example:
            ```python
            @component.mouseleave(swap="innerHTML", target=my_target_component)
            def handle_mouseleave(self):
                return ""  # Clear the hover info when mouse leaves
            ```
        """
        return self.on_event("mouseleave", swap, target, bind, False) 
 
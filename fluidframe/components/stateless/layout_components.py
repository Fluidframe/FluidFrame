from typing import Optional, Union, List
from fluidframe.core import div, p, h1, h2, h4
from fluidframe.components.stateless.text_components import Text
from fluidframe.core.components import StatelessComponent, Component, Root


class Column(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], width: Union[str, float], height: Union[str, float], vertical_alignment: str="top") -> None:
        super().__init__(parent, None)
        self.width = width
        self.height = height
        self.vertical_alignment = vertical_alignment

    def render(self) -> str:
        pass
    
    
class Container(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], height: Optional[int]=None, border:bool=False, vertical_alignment: str="top", horizontal_alignment: str="left") -> None:
        """_summary_

        Args:
            parent (Union[Component, Root]): _description_
            height (Optional[int]): Desired height of the container expressed in pixels. If None (default) the container grows to fit its content. If a fixed height, scrolling is enabled for large content and a grey border is shown around the container to visually separate its scroll surface from the rest of the app.
            border (Bool): Weather to display a border for the container or not. Default is `False` 
            vertical_alignment (str, optional): Alignment of the containers child in vertical direction values can be `top`, `middle`, `bottom`. Defaults to "top".
            horizontal_alignment (str, optional): Alignment of the containers child in horizontal direction values can be `left`, `center`, `right`. Defaults to "left".
        """
        super().__init__(parent, None)
        self.height = height
        self.border = border
        self.childern = []
        self.vertical_alignment = vertical_alignment
        self.horizontal_alignment = horizontal_alignment

    def render(self) -> str:
        # Base classes for the container
        classes = ["flex", "w-full"]
        
        if self.border:
            classes.extend(["border", "border-gray-700 dark:border-gray-100"])

        # Height classes
        if self.height is not None:
            classes.extend([f"h-[{self.height}px]", "overflow-y-auto"])
        else:
            classes.append("h-auto")

        # Vertical alignment classes
        if self.vertical_alignment == "top":
            classes.append("items-start")
        elif self.vertical_alignment == "middle":
            classes.append("items-center")
        elif self.vertical_alignment == "bottom":
            classes.append("items-end")

        # Horizontal alignment classes
        if self.horizontal_alignment == "left":
            classes.append("justify-start")
        elif self.horizontal_alignment == "center":
            classes.append("justify-center")
        elif self.horizontal_alignment == "right":
            classes.append("justify-end")

        # Combine all classes
        class_string = " ".join(classes)

        return div([child for child in self.childern], cls=class_string, id=self.id)



class Empty(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, **kwargs) -> None:
        super().__init__(parent, key, **kwargs)
        
    def render(self) -> str:
        return div(id=self.id)
        

class NavBar(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, **kwargs) -> None:
        super().__init__(parent, key, **kwargs)
    
    def render(self) -> str:
        pass
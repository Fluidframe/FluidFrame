from typing import Optional, Union
from fluidframe import Component
from fluidframe.core import div, p, h1, h2, h4


class Column(Component):
    def __init__(self, width: Union[str, float], height: Union[str, float], vertical_alignment: str="top") -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.vertical_alignment = vertical_alignment

    def render(self) -> str:
        pass
    
    
class Container(Component):
    def __init__(self, height: Optional[int]=None, border:bool=False, vertical_alignment: str="top", horizontal_alignment: str="left") -> None:
        super().__init__()
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



class Empty(Component):
    def __init__(self) -> None:
        super().__init__()
        
    def render(self) -> str:
        return div(id=self.id)
        

class NavBar(Component):
    def __init__(self) -> None:
        super().__init__()
    
    def render(self) -> str:
        pass
    
    
class SideBar(Component):
    def __init__(self) -> None:
        super().__init__()
    
    def render(self) -> str:
        pass
    

class Expander(Component):
    def __init__(self) -> None:
        super().__init__()
        
    def render(self) -> str:
        pass


class Form(Component):
    def __init__(self) -> None:
        super().__init__()
        
    def render(self) -> str:
        pass
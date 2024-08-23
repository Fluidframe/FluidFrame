from fluidframe.core import button
from fluidframe import Component
from typing import Union, Callable, Any

class Button(Component):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def render(self) -> str:
        return button(self.label, cls="bg-blue-500 m-5 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded", id=self.id)

    
class DownloadButton(Component):
    def __init__(self) -> None:
        super().__init__()
        
    def render(self) -> str:
        pass
    
class FileUploader(Component):
    def __init__(self) -> None:
        super().__init__()
        
    def render(self) -> str:
        pass
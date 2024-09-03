from fluidframe.core import Component
from fluidframe.core import p, button, div, h2

class Button(Component):
    def __init__(self, label: str, state:dict=None) -> None:
        super().__init__()
        self.label = label
        self.use_state(state, exclude_attributes=True)

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")

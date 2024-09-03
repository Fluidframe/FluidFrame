from fluidframe.core import Component
from fluidframe.core import p, button, div, h2

class Header(Component):
    def __init__(self, body: str, state:dict=None) -> None:
        super().__init__()
        self.body = body
        self.text_id = f"{self.id}-text"
        self.use_state(state, exclude_attributes=True)
        
    def render(self) -> str:
        return div(
            h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
            id=self.id
        )
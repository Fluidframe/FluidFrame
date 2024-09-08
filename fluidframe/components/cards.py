from fluidframe.core import Component
from fluidframe.core import p, button, div, h2

class Card(Component):

    def render(self) -> str:
        return div(
            self.render_children(),
            id=self.id, cls="max-w-lg mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )
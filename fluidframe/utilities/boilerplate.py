import os
from fluidframe.utils import get_lib_path

def generate_fluidframe_boilerplate(fluidframe_dir):
    boilerplate = """import uvicorn
from fluidframe.core import FluidFrame, State
from fluidpack.components import Card, Header, Button


app = FluidFrame(dev_mode=False)


###############
# Counter app #
###############

card = Card()
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")
header = Header("The count is 0", {'count': 0})

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



app.add_children(
    card.add_children(
        increment_btn, 
        header, 
        decrement_btn
    )
)


app.build()


if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
    """

    config_path = os.path.join(fluidframe_dir, 'app.py')
    with open(config_path, 'w') as f:
        f.write(boilerplate)
        
    print(f"Generated fluidframe boilerplate code at {fluidframe_dir}")
    
    
def generate_fluidframe_component_boilerplate(fluidframe_dir):
    boilerplate = """from fluidframe.core import Component
from fluidframe.core import p, button, div, h2

class Button(Component):
    def __init__(self, label: str, state:dict=None) -> None:
        super().__init__()
        self.label = label
        if state:
            self.use_state(state)

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")


class Card(Component):
    def __init__(self, state:dict=None) -> None:
        super().__init__()
        if state:
            self.use_state(state)

    def render(self) -> str:
        return div(
            [child.render() if isinstance(child, Component) else child for child in self.children],
            id=self.id, cls="max-w-lg mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )


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
    """
    
    config_path = os.path.join(fluidframe_dir, 'components.py')
    with open(config_path, 'w') as f:
        f.write(boilerplate)
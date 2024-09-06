import os


def generate_app_boilerplate(fluidframe_dir: str):
    boilerplate = """import uvicorn
from src.components import Card, Header
from fluidframe.components.buttons import Button
from fluidframe.core import FluidFrame, State, Page


app = FluidFrame(dev_mode=False)
app.mount_fluidbuild("../fluidbuild")


###############
# Counter app #
###############


card = Card()
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")
header = Header("The count is 0", {'count': 0})
page = Page(endpoint="/", title="Fluidframe Sample App")


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



app.set_entry_page(
    page(
        card(
            increment_btn, 
            header, 
            decrement_btn
        )
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
    
    
def generate_component_boilerplate(fluidframe_dir: str):
    boilerplate = """from fluidframe.core import div, h2
from fluidframe.core import Component


class Card(Component):

    def render(self) -> str:
        return div(
            self.render_children(),
            id=self.id, cls="max-w-lg mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )


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
"""
    
    config_path = os.path.join(fluidframe_dir, 'components.py')
    with open(config_path, 'w') as f:
        f.write(boilerplate)
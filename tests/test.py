import uvicorn, json
from typing import Tuple
from fluidframe.core import p, div, h2
from fluidframe.core import FluidFrame, Component
from fluidframe.components.action_components import Button
from fluidframe.components.text_components import Text, Header, Code


app = FluidFrame(dev_mode=False)

def set_state(self) -> str:
    return f"state='{json.dumps(self.state)}'"

class Header(Component):
    def __init__(self, body: str, state:dict) -> None:
        super().__init__()
        self.body = body
        self.text_id = f"{self.id}-text"
        self.use_state(state) # this will create a new dict including the once from state and the ones specific to the component like `body` and `text_id` and keeps in `self.state`
        
    def render(self) -> str:
        return div(
            h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
            id=self.id, cls="relative", state=self.set_state() # This sets the state of the dependent once as attribute
        )

# the header will have a 'state' attribute with {'count':0} as visible state as attribute and {'body': self.body, 'help': self.help, 'count': count} as the internal specific to this corresponding to its id
header = Header(
    body="Here we show a dynamic number", 
    state={'count':0} 
)


increment_btn = Button(label="Increment")
decrement_btn = Button(label="Decrement")

@increment_btn.on_event(trigger="click", target=header.text_id, bind_state=[header], action="innerHTML")

# When htmx wrap is made we will add an attribute 'bind-state' to the button which will contains the states of the nearest one with 'state' attribute, and its own self.
# So the returned json in the header will be like {'header-f74hf4': {'body': self.body, 'help': self.help, 'count': count}, 'label': 'Increment'} 

def increment(state: dict) -> Tuple[str, dict]:
    state[header.id]['count']+=1
    state['label']=f"Incremented to {state[header.id]['count']}"
    return f"You have clicked the button to increment {state['count']}", state


@decrement_btn.on_event(trigger="click", target=header.text_id, bind_state=[header], action="innerHTML")
def decrement(state: dict) -> str:
    state[header.id]['count']-=1  
    state['label']=f"Decremented to {state[header.id]['count']}"
    return f"You have clicked the button to decrement {state['count']}", state


app.child(increment_btn)
app.child(header)
app.child(decrement_btn)


app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
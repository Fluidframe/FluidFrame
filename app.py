import uvicorn
from fluidframe.core import p
from fluidframe.core import FluidFrame, Component
from fluidframe.components.action_components import Button
from fluidframe.components.text_components import Text, Header, Code


app = FluidFrame(dev_mode=False)


###################################
# Shows two buttons with a header #
###################################
n=0
header = Header("Here we show a dynamic number", help="This will change when the button is clicked")

increment_btn = Button("Increment")
@increment_btn.on_event(trigger="click", target=header, action="innerHTML", transition=True, cache=False)
def increment() -> str:
    global n, header
    n+=1
    header.body=f"You have clicked the button to increment {n}"
    return header.render()

decrement_btn = Button("Decrement")
@decrement_btn.on_event(trigger="click", target=header, action="innerHTML", transition=True, cache=False)
def decrement() -> str:
    global n, header
    n-=1         
    header.body=f"You have clicked the button to decrement {n}"
    return header.render()


app.child(increment_btn)
app.child(header)
app.child(decrement_btn)



#########################
# Displays a code block #
#########################
code_block = """# This is a code block
import numpy as np
import fluidframe as ff

def myfunc():
    return ff.header("This is a fluidframe header").render()
    
print("Cool")
"""

code = app.child(Code(code_block, "python"))


####################
# Loading contents #
####################
    
btn = app.child(Button("Load More"))

# A quick component #
class Item(Component):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
    
    def render(self) -> str:
        return p(self.text, id=self.id, cls="m-5 border border-gray-300 p-5 text-center rounded-lg shadow-lg")   
       
       
t1 = app.child(Item("Loaded Section"))
t2 = app.child(Item("Loaded Section")) 

@btn.on_event(trigger="click", target=[t1, t2], action="outerHTML", cache=False, transition=True)  #
def load_more() -> str:   
    return t1.render() + t2.render()


app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
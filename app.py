import uvicorn
from fluidframe.core import p, button, div, h2
from fluidframe.core import FluidFrame, Component


app = FluidFrame(dev_mode=False)


####################
# A simple counter #
####################
class Button(Component):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg ")

class Card(Component):
    def __init__(self) -> None:
        super().__init__()

    def render(self) -> str:
        return div(
            [child.render() for child in self.children],
            id=self.id, cls="max-w-md mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )

class Header(Component):
    def __init__(self, body: str) -> None:
        super().__init__()
        self.count = 0
        self.body = body
        self.text_id = f"{self.id}-text"
        self.use_state(include='count')
        
    def render(self) -> str:
        return div(
            h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
            id=self.id, cls="relative", state=self.set_state()
        )


card = Card()
header = Header("The count is 0")
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")

@increment_btn.click(swap="innerHTML", target=header.text_id, bind_state=header)
def increment(state) -> str:
    state['count']+=1
    return f"The count is {state['count']}", state


@decrement_btn.click(swap="innerHTML", target=header.text_id, bind_state=header)
def decrement(state) -> str:
    state['count']-=1
    return f"The count is {state['count']}", state


app.add_children(
    card.add_children(
        increment_btn, 
        header, 
        decrement_btn
    )
)


####################
# Loading contents #
####################
btn = app.child(Button("Load More"))

# A quick component #
class Item(Component):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
        self.item_number = 1
        self.use_state(include='item_number')
    
    def render(self) -> str:
        return p(self.text, id=self.id, cls="m-5 border border-gray-300 p-5 text-center rounded-lg shadow-lg", state=self.set_state())   
       
       
list1 = app.child(Item("Loaded Section number 1"))
list2 = app.child(Item("Loaded Section number 2"))

@btn.click(target=list2, swap="outerHTML", bind_state=list1)
def load_more(state) -> str: 
    state['item_number']+=1
    list3 = Item(f"Loaded Section number {state['item_number']}") 
    state['item_number']+=1
    list4 = Item(f"Loaded Section number {state['item_number']}") 
    return list3.render(), list4.render(), state


app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8080, reload=True)
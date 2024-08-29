import uvicorn, json
from fluidframe.core import p, button, div, h2
from fluidframe.core import FluidFrame, Component, State


app = FluidFrame(dev_mode=False)


####################
# A simple counter #
####################
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

card = Card()
header = Header("The count is 0", {'count': 0})
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")

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


####################
# Loading contents #
####################

# A quick component #
class Item(Component):
    def __init__(self, text: str, state:dict=None) -> None:
        super().__init__()
        self.text = text
        if state:
            self.use_state(state)
    
    def render(self) -> str:
        return p(self.text, id=self.id, cls="m-5 border border-gray-300 p-5 text-center rounded-lg shadow-lg")


btn = Button("Load More")
card2 = Card()
card3 = Card()
item = Item(f"Item number: 1", {'item_count': 1})
card3.child(item)


@btn.click(target=card3, swap="beforeend", bind=item)
def load_more(state: State) -> str: 
    count = state.get('item_count')
    count+=1
    state.set('item_count', count)
    return Item(f"Item number: {count}")

app.add_children(
    card2.add_children(
        Header("Items"),
        card3,
        btn,
    )
)

app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
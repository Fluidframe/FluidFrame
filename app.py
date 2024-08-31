import uvicorn
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
    
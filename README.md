# FluidFrame

<p align="center">
  <img src="./fluidframe/public/assets/fluidframe-logo.webp" alt="FluidFrame Logo" />
</p>


FluidFrame is a powerful, pythonic web application framework that embraces the simplicity and capability of hypermedia concepts. It combines Python's elegance with HTMX's innovative approach to create dynamic, interactive web applications without the need for complex JavaScript.

## Key Features

- **Hypermedia-Driven**: Utilizes HTMX to implement Hypermedia as the Engine of Application State (HATEOAS), allowing the server to control the flow of information and interactions.

- **Pythonic HTML Generation**: Create HTML structures using Python syntax, making your code more consistent and easier to maintain.

```python
content = html(
    div(
        h1("Welcome to FluidFrame", cls="heading"),
        p("Build powerful web apps with Python elegance", cls="description"),
        a("Get Started", href="/docs", cls="btn"),
        cls="container", id="welcome_section"
    )
)
```

- **Component-Based Architecture**: Build your UI with reusable, Python-defined components, promoting code organization and reusability.

```python
from fluidframe.core import p, button, div, h2
from fluidframe.core import FluidFrame, Component, State

class Button(Component):
    def __init__(self, label: str, state:dict=None) -> None:
        super().__init__()
        self.label = label
        self.use_state(state, exclude_attributes=True)

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")


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


card = Card()
header = Header("The count is 0", {'count': 0})
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")

app.add_children(
    card(
        increment_btn, 
        header, 
        decrement_btn
    )
)
```

- **Automatic Route Generation**: Simplify your development process with automatic route generation for HTMX-enabled components.
- **Full-Stack Python**: Develop entire web applications using Python, from backend logic to frontend interactions, without writing JavaScript or HTML.
- **High Performance**: Utilizes Cython for core HTML tag generation, offering speed comparable to or faster than traditional templating engines like Jinja2.
Pre-built Components: Jump-start your development with a library of pre-built, customizable UI components.
- **Pre-built Components**: Jump-start your development with a library of pre-built, customizable UI components which are similar to that of `streamlit` so for those who knows it fluidframe becomes a piece of cake **without the full code rerun of streamlit**.

## Example
### Here's a simple example of a text component in FluidFrame with and without a tooltip:


---

### Simple button:
```python
from fluidframe.core import button
from fluidframe.core import Component

class Button(Component):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")

```

---

### Simple counter application:
```python
import uvicorn
from fluidframe.core import FluidFrame, Component

app = FluidFrame(dev_mode=False)


class Button(Component):
    def __init__(self, label: str, state:dict=None) -> None:
        super().__init__()
        self.label = label
        self.use_state(state, exclude_attributes=True)

    def render(self) -> str:
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")


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
    card(
        increment_btn, 
        header, 
        decrement_btn
    )
)

app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
```

---

### Simple application which loads more content when button clicked
```python
import uvicorn
from fluidframe.core import FluidFrame, Component

class Item(Component):
    def __init__(self, text: str, state:dict=None) -> None:
        super().__init__()
        self.text = text
        self.use_state(state, exclude_attributes=True)
    
    def render(self) -> str:
        return p(self.text, id=self.id, cls="m-5 border border-gray-300 p-5 text-center rounded-lg shadow-lg")


class Card(Component):
    def render(self) -> str:
        return div(
            self.render_children(),
            id=self.id, cls="max-w-lg mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )

btn = Button("Load More")
card1 = Card()
card2 = Card()
item = Item(f"Item number: 1", {'item_count': 1})


@btn.click(target=card2, swap="beforeend", bind=item)
def load_more(state: State): 
    count = state.get('item_count')
    count+=1
    state.set('item_count', count)
    return Item(f"Item number: {count}")


app.add_children(
    card1(
        card2(
            item 
            # When button is pressed we add more items in DOM dynamically
        ),
        btn,
    )
)

app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
```

---

## Developments

- `Aug 29, 2024`: Added multiple event trigger binding onto any fluidframe components. This required us to make a custom attribute to programatically set the event listeners to trigger htmx ajax calls. We use `hx-trigger-info` tag with an html escaped json string which will have necessary htmx related informations per trigger event to set the event listeners.

- `Aug 26, 2024`: Added support for state management of components. Fluidframe components stores the state in client side and the state updates are controlled by the server side along with htmx response modifiers to modify HTMX behaviours and client side event triggering controls. 

- `Aug 9, 2024`: Automatic client side dependency management. Dependency scripts and styles in Fluidframe applications are loaded on demand based or requirement of a component. This drastically reduces initial load times because only the necessary scripts and styles are loaded and further scripts are loaded depending on mounting of new components. Once loaded they are not needed to be loaded again as they persist in local storage. (Currently tailwind's generated css is completly passed to the client, we need to make something similar to purge css to only extract the required style content to be passed to the client)

    
---

## Why FluidFrame?

FluidFrame simplifies web development by leveraging the power of hypermedia and the simplicity of Python. It allows developers to create interactive, full-stack web applications without the complexity of traditional JavaScript frameworks. By using HTMX under the hood, FluidFrame enables rich, dynamic user experiences while keeping your codebase clean, maintainable, and purely Python-based.

Whether you're building a small web app or a large-scale application, FluidFrame provides the tools and structure to make your development process smooth and efficient.

Get started with FluidFrame today and experience the joy of building modern web applications with pure Python!

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher
- Poetry (for dependency management)
- A C compiler (GCC on Linux/macOS, or Microsoft Visual C++ on Windows)
    - On Windows: You'll need Microsoft Visual C++. The easiest way to get this is to install "Build Tools for Visual Studio".
    - On macOS: You can use Xcode's command-line tools. Install them by running `xcode-select --install` in the terminal.
    - On Linux: You likely already have GCC installed. If not, you can install it using your distribution's package manager (e.g., `sudo apt-get install gcc` on Ubuntu).

    **Note:** Python development headers are usually included with Python, but on some systems, you might need to install them separately. On Ubuntu or Debian, for example, you might need to install `python3-dev`.


## Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/AswanthCManoj/fluidframe.git
cd fluidframe
```

2. Install the project dependencies using Poetry:

```bash
poetry install
```

**Note: BY default currently its in development mode which creates a `node modules` folder within the libraries folder for development purpose**
This step also compiles the Cython modules and places the resulting binary files in the appropriate directories.

3. Initialize a project:

```bash
poetry run fluidframe init myproject
```

4. Verify the installation:
```bash
poetry shell
python

from fluidframe.core import div

print(div("This is a div tag"))
```

If you see "Installation successful!" printed without any errors, the installation is complete.

---

> **For seeing sample usage check out the example in [`app.py`](./app.py)**

**Note**: 
- All the components will have the ability to set an `event` when used as a decorator over a function the function will be considered as the even handler


## ToDo
- Adding support for pages
- Proper structuring for folders created after `fluidframe init <myproject>`
- `fluidframe install <package>` should also re-analyze the node_modules folder to generate the folder mapping.
- Implementing purge css with python regular expressions implementations to trim on styles served via on-demand component dependecies file injection.
- Adding options for efficient javscript bundling to bundle up only the required features for fluidpack.


## Future Directions

- Using [`Robyn`](https://github.com/sparckles/Robyn) as the webframework backend along with optimised rendering codes written in Rust
- **FluidPack** A component library extension having fluidframe custom components. The following sample components will be available shortly: `Text`, `Markdown`, `Latex`, `Title`, `Header`, `SubHeader`, `Caption`, `Code`, `Image`, `Audio`, `Video`, `Diagram`, `Button`, `TextInput`, `TextArea`, `Slider`, `SelectBox`, `MultiSelectBox`, `CheckBox`, `Radio`, `DateInput`, `TimeInput`, `FileUploader`, `ColorPicker()`, `DownloadButton`, `Progress`, `Spinner`, `Status`, `Form`, `Column`, `Container`, `SideBar`, `Expander`, `Empty`, `NavBar`.
- A `streamlit`'s component API like extension using fluidframe. 

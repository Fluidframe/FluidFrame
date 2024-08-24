# FluidFrame

<p align="center">
  <img src="./fluidframe/public/assets/fluidframe-logo.webp" alt="FluidFrame Logo" />
</p>


FluidFrame is a powerful, pythonic web application framework that embraces the simplicity and capability of hypermedia concepts. It combines Python's elegance with HTMX's innovative approach to create dynamic, interactive web applications without the need for complex JavaScript.

## Key Features

- **Hypermedia-Driven**: Utilizes HTMX to implement Hypermedia as the Engine of Application State (HATEOAS), allowing the server to control the flow of information and interactions.

- **Component-Based Architecture**: Build your UI with reusable, Python-defined components, promoting code organization and reusability.

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
- **Automatic Route Generation**: Simplify your development process with automatic route generation for HTMX-enabled components.
- **Full-Stack Python**: Develop entire web applications using Python, from backend logic to frontend interactions, without writing JavaScript or HTML.
- **High Performance**: Utilizes Cython for core HTML tag generation, offering speed comparable to or faster than traditional templating engines like Jinja2.
Pre-built Components: Jump-start your development with a library of pre-built, customizable UI components.
- **Pre-built Components**: Jump-start your development with a library of pre-built, customizable UI components which are similar to that of `streamlit` so for those who knows it fluidframe becomes a piece of cake **without the full code rerun of streamlit**.

## Example
### Here's a simple example of a text component in FluidFrame with and without a tooltip:

```python
from fluidframe.core import div, p
from fluidframe.core import Component
from fluidframe.core.dependency import requires
from fluidframe.public import js_bundle as public_files
from fluidframe.utilities.package_manager import url_for_public

class Text(Component):
    def __init__(self, body: str, help: Optional[str]=None) -> None:
        super().__init__()
        self.body = body
        self.help = help 
        self.scripts=url_for_public(public_files.scripts.tooltip_js)
        
    def render(self) -> str:
        if self.help:
            return div(
                requires(self.scripts),
                p(self.body, cls="text-sm text-gray-900 dark: text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 mx-5 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative", onmouseenter=show_tooltip(self.id), onmouseleave=hide_tooltip(self.id)
            )
        return div(
            p(self.body, cls="text-sm text-gray-900 dark: text-white"), 
            id=self.id, cls="relative"
        )
```

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
        return button(self.label, cls="bg-blue-500 m-5 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded", id=self.id)

```

---

### Simple counter application:
```python
import uvicorn
from fluidframe.core import FluidFrame, Component
from fluidframe.components.text_components import Header
from fluidframe.components.action_components import Button

app = FluidFrame(dev_mode=False)

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

app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
```

---

### Simple application which loads more content when button clicked
```python
import uvicorn
from fluidframe.core import FluidFrame, Component
from fluidframe.components.text_components import Header
from fluidframe.components.action_components import Button

btn = app.child(Button("Load More"))

# A quick component
class Item(Component):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
    
    def render(self) -> str:
        return p(self.text, id=self.id, cls="m-5 border border-gray-300 p-5 text-center rounded-lg shadow-lg")   
       

t1 = app.child(Item("Loaded Section"))
t2 = app.child(Item("Loaded Section")) 

@btn.on_event(trigger="click", target=[t1, t2], action="outerHTML", cache=False, transition=True)
def load_more() -> str:   
    return t1.render() + t2.render()

app.build()
if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
```

---

## Developments

- FluidFrame utilizes a Cython implementation for HTML tags, resulting in a speed boost for small scale template rendering when compared to Jinja2.

    In a performance test involving 1,000,000 iterations, FluidFrame's tag rendering was approximately 9.58 times faster than Jinja2 at small scale rendering.

    | Iterations | fluidframe tags | jinja2 |
    |---|---|---|
    1,000,000|0.7361083286003123s|7.126994657999967s|

    This speed advantage can be crucial for our specific case of htmx response rendering as the scale and depth of required html will be smaller.

    At the same time when child elements are higher to loop through (>10000) Jinja2 is consistently faster. But since we are using HTMX and its support for server sent events allow us to sent the data dynamically as its been generated and rendered there by closing the gap.

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

## Components
The following sample components will be available, but its easy to make your own on the fly
`Text`, `Markdown`, `Latex`, `Title`, `Header`, `SubHeader`, `Caption`, `Code`, `Image`, `Audio`, `Video`, `Diagram`, `Button`, `TextInput`, `TextArea`, `Slider`, `SelectBox`, `MultiSelectBox`, `CheckBox`, `Radio`, `DateInput`, `TimeInput`, `FileUploader`, `ColorPicker()`, `DownloadButton`, `Progress`, `Spinner`, `Status`, `Form`, `Column`, `Container`, `SideBar`, `Expander`, `Empty`, `NavBar`


> **For seeing sample usage check out the example in [`app.py`](./app.py)**

**Note**: 
- All the components will have the ability to set an `event` when used as a decorator over a function the function will be considered as the even handler


## Future Directions

- Adding bidirectional state management
- Inlineuse of predefined scripts without messing with browser contant policy
- Using [`Robyn`](https://github.com/sparckles/Robyn) as the webframework backend along with optimised rendering codes written in Rust

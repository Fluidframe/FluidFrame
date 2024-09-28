# FluidFrame

<p align="center">
  <img src="./fluidframe/public/assets/fluidframe-logo.webp" alt="FluidFrame Logo" />
</p>


FluidFrame is a cutting-edge web application framework that brings together the power of Python and the innovation of hypermedia concepts. At its core, FluidFrame is designed to simplify web development while delivering dynamic, interactive applications without the complexity typically associated with JavaScript frameworks.

Built on the principles of Hypermedia as the Engine of Application State (HATEOAS) and leveraging HTMX, FluidFrame allows developers to create rich, responsive web applications using pure Python. It combines the elegance and readability of Python with the interactivity of modern web apps, offering a unique approach to full-stack development.

FluidFrame introduces a component-based architecture, automatic route generation, and high-performance HTML generation through Cython. It also provides a set of pre-built, customizable UI components inspired by popular frameworks like Streamlit, but with improved performance and flexibility.

**It's perfect for those of us who'd rather wrestle a real python than deal with JavaScript promises!**



---

## Key Features

- **Hypermedia-Driven**: Utilizes HTMX to implement Hypermedia as the Engine of Application State (HATEOAS). Your server becomes the puppet master, pulling all the strings of your app's interactions. Dance, little web elements, dance! 🎭🕺

- **Pythonic HTML Generation**: Create HTML structures using Python syntax. Who said you can't have your Python cake and eat HTML too? 🐍🎂

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

- **Component-Based Architecture**: Build your UI with reusable, Python-defined components. It's like React had a Python-powered glow-up. Who said snakes can't be component creatures? 🐍🧩

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
    ```

- **Automatic Route Generation**: Simplify your development process with automatic route generation. Say goodbye to the days of manually mapping routes like a lost explorer. Columbus wishes he had this! 🧭🌎

- **Full-Stack Python**: Build entire web apps using nothing but Python, from backend wizardry to frontend magic—no need to cheat on Python with JavaScript. Stay loyal to your favorite snake! 🐍✨

- **High Performance**: Utilizes Cython for core HTML tag generation. We've turbocharged your Python so much, it might just achieve time travel. Great Scott! 🚀⏱️

- **Pre-built Components**: Jump-start your development with a library of pre-built, customizable UI components. It's the all-you-can-code buffet, and we've already done the cooking! 👨‍🍳🍽️

- **Streamlit-inspired Components**: Love Streamlit's simplicity but hate the constant reruns? We've brought your favorite components to the party, minus the marathon running and object destruction. It's like Streamlit went to charm school and learned some new tricks! 🎓🪄



---

## Why FluidFrame?

FluidFrame was born out of a desire to simplify web development while addressing common pain points in modern frameworks. At its core, FluidFrame embraces the principle that web development shouldn't require juggling multiple languages or dealing with the complexities of heavy client-side JavaScript frameworks.

By leveraging Python's elegance and the power of hypermedia, FluidFrame offers a unique approach to building interactive web applications. It eliminates the need for large initial bundle loads, reducing page load times and providing a snappier user experience from the start. The framework's design recognizes that users typically interact with one element at a time, optimizing performance by updating only what's necessary.

FluidFrame simplifies the data flow between frontend and backend, removing the need for separate JSON APIs and client-side rendering logic. This streamlined approach means developers can add or modify features in one place, reducing complexity and potential for errors. It also embraces progressive enhancement, ensuring that applications remain functional even if JavaScript fails, thus improving accessibility and robustness.

For Python developers, FluidFrame offers a familiar environment to build full-stack applications without leaving their preferred language. It combines the best aspects of frameworks like React and Streamlit, offering component-based architecture and easy-to-use UI elements, but with improved performance and flexibility.

Ultimately, FluidFrame is about empowering developers to create modern, responsive web applications with less cognitive overhead. It's for those who want to focus on building features rather than wrestling with web technologies, all while leveraging the full power of Python across the entire stack. With FluidFrame, you can experience the joy of building interactive, efficient web applications that are a breeze to develop and maintain.



---

## Prerequisites
Before you begin, ensure you have the following installed on your system:

- Python 3.8 or higher (because we're not savages)
- Poetry (for dependency management, and because real Pythonistas write poetry)
- A C compiler (GCC on Linux/macOS, or Microsoft Visual C++ on Windows)
    - On Windows: You'll need Microsoft Visual C++. The easiest way to get this is to install "Build Tools for Visual Studio". Yes, we know, it's Windows. We're sorry.
    - On macOS: You can use Xcode's command-line tools. Install them by running `xcode-select --install` in the terminal. It's like giving your Mac a tiny developer superpower!
    - On Linux: You likely already have GCC installed. If not, you can install it using your distribution's package manager (e.g., `sudo apt-get install gcc` on Ubuntu). Linux users, you're the real MVPs!

    **Note:** Python development headers are usually included with Python, but on some systems, you might need to install them separately. On Ubuntu or Debian, for example, you might need to install `python3-dev`.



---

## Installation and development

### contributing
  1. Clone the repository:
  ```bash
  git clone https://github.com/Fluidframe/FluidFrame.git
  cd fluidframe
  ```
    
  2. Install the project dependencies using Poetry:
  ```bash
  poetry install
  poetry run pip install -e .
  ```
  
### Development
  Install FluidFrame directly from the repository:
  - Using pip:
  ```bash
  pip install git+https://github.com/Fluidframe/FluidFrame.git
  ```
       
  - Using Poetry:
  ```bash
  poetry add git+https://github.com/Fluidframe/FluidFrame.git
  ```

**Note:** This step compiles the Cython modules and places the resulting binary files in the appropriate directories. (Currently only supports Linux)


### Project Initialization
Create a new FluidFrame project:
```bash
poetry run fluidframe init myproject
```
This command creates two folders:

- `fluidbuild`: Contains all module dependencies and related files
- `src`: Contains starter boilerplate code


### Verification
To verify the installation:
```bash
poetry shell
python
```
Then in the Python interpreter:
```bash
from fluidframe.core import div
print(div("Installation successful!"))
```

If you see `<div>Installation successful!</div>` printed without any errors, the installation is complete.



---

## FluidFrame CLI Commands

FluidFrame comes with a powerful Command Line Interface (CLI) to help you manage your projects efficiently. Here are the available commands:

**(For those moments when you want to feel like a hacker in a movie, but with less illegal activity and more web development)**

### Initialize a New Project
```bash
fluidframe init <project_name>
```
This command initializes a new FluidFrame project with the given name. It sets up the necessary folder structure and configuration files.

### Install a Node.js Package
```bash
fluidframe install <package_name>
```
Installs a Node.js package in your FluidFrame project. When you absolutely, positively need that one JavaScript library. We won't judge... much.

### Uninstall a Node.js Package
```bash
fluidframe uninstall <package_name>
```
Oops, changed your mind? No worries, we'll help you break up with that package **(Removes a Node.js package from your FluidFrame project.)**

### Update Node.js Packages
```bash
fluidframe update
```
Keep your packages fresh, unlike that milk in your fridge.

### Build Tailwind CSS
```bash
fluidframe build-css
```
Builds the Tailwind CSS for your project, generating optimized styles.

### Bundle JavaScript
```bash
fluidframe bundle --input <input_dir> --output <output_dir>
```
Bundles JavaScript files using Rollup. By default, it uses 'src' as the input directory and 'fluidbuild/dist' as the output directory.

### Generate Source Map
```bash
fluidframe map <folder_path>
```
Generates a source map for the specified directory, creating an easy-to-use structure for accessing your project's files.

These CLI commands streamline your development workflow, making it easier to manage dependencies, build assets, and organize your FluidFrame projects.



---

## Example

Here are some examples demonstrating the simplicity and power of FluidFrame:

### 1. Simple Button Component

This example shows how to create a basic button component:

```python
from fluidframe.core import button, Component

class Button(Component):
    def __init__(self, label: str) -> None:
        super().__init__()
        self.label = label

    def render(self) -> str:
        # Return a button with Tailwind CSS classes for styling
        return button(self.label, id=self.id, cls="bg-blue-500 text-xl m-5 hover:bg-blue-700 text-white font-bold py-2 px-5 rounded-lg")

```

### Counter Application

This example demonstrates a simple counter application with increment and decrement functionality:

```python
import uvicorn
from fluidframe.components.buttons import Button
from fluidframe.core import FluidFrame, State, Page, div, h2


app = FluidFrame()


class Card(Component):
    def render(self) -> str:
        # Create a card container for our components
        return div(
            self.render_children(),
            id=self.id,
            cls="max-w-lg mx-auto mt-20 p-10 shadow-lg rounded-lg flex flex-col items-center justify-center space-y-5 bg-white/10 backdrop-blur-md border border-white/20"
        )

class Header(Component):
    def __init__(self, body: str, state: dict = None) -> None:
        super().__init__()
        self.body = body
        self.text_id = f"{self.id}-text"
        self.use_state(state, exclude_attributes=True)
        
    def render(self) -> str:
        return div(
            h2(self.body, id=self.text_id, cls="text-4xl text-gray-900 font-bold dark:text-white"),
            id=self.id
        )

# Create instances of our components
card = Card()
increment_btn = Button("Increment")
decrement_btn = Button("Decrement")
header = Header("The count is 0", {'count': 0})
page = Page(endpoint="/", title="FluidFrame Sample App")

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


# Set up the page structure
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
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
```

### Dynamic Content Loading

This example shows how to dynamically load content when a button is clicked:

```python
import uvicorn
from fluidframe.components.buttons import Button
from fluidframe.core import FluidFrame, Component, State, Page

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
page = Page(endpoint="/", title="Fluidframe Sample App")


@btn.click(target=card2, swap="beforeend", bind=item)
def load_more(state: State): 
    count = state.get('item_count')
    count+=1
    state.set('item_count', count)
    return Item(f"Item number: {count}")


# Set up the page structure
app.set_entry_page(
    page(
        card1(
            card2(
                item 
                # When button is pressed, we add more items to the DOM dynamically
            ),
            btn,
        )
    )
)

app.build()

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000)
```

These examples demonstrate how FluidFrame allows you to create interactive web applications using pure Python. The framework handles the complexities of state management and DOM updates, allowing you to focus on your application logic.



---

## Developments

- `Sep 5, 2024`: Fluidframe cli now supports folder mapping and javascript bundling. 

    - **Folder mapping**: FluidFrame's CLI now includes a powerful map command that simplifies file and asset management in your projects. By running `fluidframe map path/folder`, the CLI generates a Python file that creates an easy-to-use structure for accessing your project's files. For example, after mapping, you can access files like this:

        ```python
        from path.folder import js_bundle as folder
        image_path = folder.images.my_image_png  # Gets path to './path/folder/images/my_image.png'
        ```
        This feature provides IDE support with autocompletion, reduces errors from manual path typing. It's a small change that makes a big difference in day-to-day development, especially for larger projects with complex file structures.

    - **Bundling**: FluidFrame now offers a powerful bundling command to optimize your component dependencies: `fluidframe bundle --input=src --output=dist`

        This command leverages Rollup behind the scenes to create efficient, tree-shaken bundles for your JavaScript and CSS dependencies. Here's how it works:

        1. Place your component-specific JavaScript files in the `src` folder. For example, to use PrismJS for Python syntax highlighting, you might have a `prism-python.js` file:

            ```javascript
            import Prism from 'prismjs/components/prism-core';
            import 'prismjs/components/prism-python.min';
            import 'prismjs/themes/prism-okaidia.css';
            ```
            
        2. Run the bundle command to process these files.
        3. FluidFrame creates optimized bundles in the `dist` folder, including only the necessary code and styles.

        Key benefits:

        - Modular dependency management at the component level
        - On-demand loading of JS and CSS, reducing initial page load times
        - Optimized bundles with tree-shaking for minimal file sizes
        - Simplified management of third-party libraries and their specific features

        This approach allows FluidFrame to maintain high performance by loading only the required dependencies for each component at runtime, rather than sending all JavaScript and CSS at initial page load.


- `Sep 3, 2024`: Added support for pages, so now you can build multipage applications instead of single page.

- `Aug 29, 2024`: Added multiple event trigger binding onto any fluidframe components. This required us to make a custom attribute to programatically set the event listeners to trigger htmx ajax calls. We use `hx-trigger-info` tag with an html escaped json string which will have necessary htmx related informations per trigger event to set the event listeners.

- `Aug 26, 2024`: Added support for state management of components. Fluidframe components stores the state in client side and the state updates are controlled by the server side along with htmx response modifiers to modify HTMX behaviours and client side event triggering controls. 

- `Aug 9, 2024`: Automatic client side dependency management. Dependency scripts and styles in Fluidframe applications are loaded on demand based or requirement of a component. This drastically reduces initial load times because only the necessary scripts and styles are loaded and further scripts are loaded depending on mounting of new components. Once loaded they are not needed to be loaded again as they persist in local storage. (Currently tailwind's generated css is completly passed to the client, we need to make something similar to purge css to only extract the required style content to be passed to the client)



---

## Future Directions

- **Robyn Integration**: We're exploring the possibility of using [Robyn](https://github.com/sparckles/Robyn) as the web framework backend instead of Starlette. Robyn's Rust-based architecture promises to bring even more speed and efficiency to FluidFrame's core.

- **Rust-Powered Core**: To squeeze out every last drop of performance, we're considering rewriting FluidFrame's core in Rust. This would allow us to leverage Rust's blazing speed and memory safety while maintaining Python's ease of use for application logic.

- **Purge CSS**: Implementing purge css with python regular expressions implementations to trim on styles served via on-demand component dependecies file injection.

- **FluidPack Component Library**: We're excited to introduce FluidPack, a comprehensive component library extension for FluidFrame. This library will offer a wide array of customizable, pre-built components to accelerate your development process. Some of the components you can look forward to include:

  `Text`, `Markdown`, `LaTeX`, `Title`, `Header`, `SubHeader`, `Caption`, `Code`, `Image`, `Audio`, `Video`, `Diagram`, `Button`, `TextInput`, `TextArea`, `Slider`, `SelectBox`, `MultiSelectBox`, `CheckBox`, `Radio`, `DateInput`, `TimeInput`, `FileUploader`, `ColorPicker`, `DownloadButton`, `Progress`, `Spinner`, `Status`, `Form`, `Column`, `Container`, `SideBar`, `Expander`, `Empty`, `NavBar`

  Each component will come with multiple themes, allowing you to easily customize the look and feel of your application.

- **Streamlit-Inspired API**: We're developing a component API inspired by Streamlit's intuitive design. This will allow developers familiar with Streamlit to quickly adapt to FluidFrame, while also providing an easy-to-use interface for building complex applications with minimal code.

These future developments are aimed at making FluidFrame not just a framework, but a complete ecosystem for web development in Python. From blazing-fast performance to a rich component library and intuitive API, we're committed to providing you with all the tools you need to build sophisticated web applications without leaving the comfort of Python.

Stay tuned as we slither towards a future where Python rules the web, one **Fluid Frame** at a time! 🐍🌊



---

## Embracing the FluidFrame Philosophy

With FluidFrame, we're not waging war against JavaScript—we use it ourselves and support other libraries. However, we believe that putting all rendering and interactivity on JavaScript's shoulders isn't always the best approach. Instead, we've chosen to think differently, embracing simplicity and cherry-picking the best ideas from various sources.

FluidFrame is more than just a framework; it's a philosophy that celebrates:

- The elegance and readability of Python
- The power of server-side rendering
- The efficiency of minimal, purposeful JavaScript

As you embark on your FluidFrame journey, imagine crafting web applications that flow as smoothly as Python code itself. We're here to make web development feel as natural and refreshing as a cool stream on a summer's day.

So, fellow Pythonistas, let's sculpt digital experiences that are as dynamic and adaptable as water itself. With FluidFrame, you're not just coding—you're creating digital art with the precision of a Python interpreter.

Welcome to the FluidFrame way of life. Let's make waves! 🐍💻🌊


## Acknowledgements

This project stands on the shoulders of giants. I'am deeply grateful to the following open-source projects and their communities:

- [Starlette](https://www.starlette.io/) - The lightweight ASGI framework powering our backend.
- [HTMX](https://htmx.org/) - The innovative library enabling our dynamic frontend with minimal JavaScript.
- [Tailwind CSS](https://tailwindcss.com/) - The utility-first CSS framework that streamlines our styling process.
- [Uvicorn](https://www.uvicorn.org/) - The lightning-fast ASGI server that runs our application.

These tools have been instrumental in building and running our project efficiently. We extend our heartfelt thanks to the developers, contributors, and maintainers of these projects for their outstanding work and continued support.


### Inspirations

Our project has been inspired by several groundbreaking frameworks and libraries:

- [React](https://github.com/facebook/react) - While we don't use React directly, its component-based architecture has influenced our approach to building user interfaces.
- [Streamlit](https://github.com/streamlit/streamlit) - Streamlit's simplicity in creating data applications has inspired aspects of our user experience design.
- [FastHTML](https://github.com/AnswerDotAI/fasthtml) - FastHTML's focus on building powerful, scalable web applications with minimal, compact code aligns closely with our project goals. Its innovative use of HTMX to build full applications while keeping everything within the Python ecosystem has inspired our own development patterns, demonstrating how to leverage HTMX's power in a Pythonic way.

We're grateful for the innovative ideas these projects have contributed to the web development ecosystem.


## A Slithery Secret

Psst! Want to know a secret? The JavaScript bits in FluidFrame were actually written by [Claude](https://claude.ai/). Because even Python devotees need a JS wingman sometimes.

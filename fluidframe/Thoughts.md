## TODOS

1. Using `webpack` to generate tree-shaken component specific bundles and then using it to generate a a json representing this tree which then can be compiled to generate a .py file containing pydantic object representations of these which allows IDE support and auto-complete for importing the same on to python components. 
**This could literally solve the issue of needing to have order in specifying the import scripts for component load at first time**

2. Server side dependency manager to identify these bundles and bind them on to the component which then be mounted to statics of starlette.

3. Creating minimal javascripts which could be binded to tags via `hx-on` with a trigger to fire interactivity.

4. Adding state objects header jsons to the HTMX requests and response to manage component state by the server without needing to keep any state in server itself. This works by adding the required `state` of the component as json to a hx request header which the server can read and modify or manipulate rendering if required and send back the updated state with the same header back to client which stored in localstorage.

5. Update the `tags` and their cython implementation to give support for html extend attributes such as `hx-on:click...` which should be created by tag parameter usage of `hx_on="click:..."`.
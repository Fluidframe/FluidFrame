from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.routing import Route
import uvicorn
from fluidframe.base import Page



async def homepage(request):
    page = Page(title="HTMX Example")
    page.add_child()
    return HTMLResponse(page.render())
    

async def more_content(request):
    return HTMLResponse("")
    

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/more-content', more_content),
])

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)


# templates = Jinja2Templates(directory='fluidframe/templates')

# return templates.TemplateResponse("/", page.render())

# return templates.TemplateResponse('more_content.html', {'request': request})
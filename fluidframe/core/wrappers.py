import inspect
from starlette.requests import Request
from typing import Callable, get_type_hints
from starlette.responses import HTMLResponse


def html_render_wrap(func: Callable) -> HTMLResponse:
    async def wrapped_func(request: Request) -> HTMLResponse:
        sig = inspect.signature(func)
        type_hints = get_type_hints(func)
        kwargs = {}
        if sig.parameters:
            for name, param in sig.parameters.items():
                if name == 'request' or (param.annotation is Request):
                    kwargs[name] = request
                    continue
                
                value = None
                # Check query params (including arrays)
                if name in request.query_params:
                    value = request.query_params.getlist(name) if len(request.query_params.getlist(name)) > 1 else request.query_params[name]
                # Check path params
                elif name in request.path_params:
                    value = request.path_params[name]
                # Check JSON body
                elif request.headers.get("Content-Type") == "application/json":
                    json_body = await request.json()
                    value = json_body.get(name)
                # Check form data (including file uploads)
                elif request.headers.get("Content-Type", "").startswith("multipart/form-data") or \
                     request.headers.get("Content-Type") == "application/x-www-form-urlencoded":
                    form = await request.form()
                    if name in form:
                        value = form[name] if not hasattr(form[name], "filename") else form[name].file
                # Check headers (including custom prefixes)
                elif name in request.headers or f"X-{name}" in request.headers:
                    value = request.headers.get(name) or request.headers.get(f"X-{name}")
                # Check cookies
                elif name in request.cookies:
                    value = request.cookies[name]
                # Type conversion
                if value is not None and name in type_hints:
                    try:
                        value = type_hints[name](value)
                    except ValueError:
                        pass  # Keep original value if conversion fails
                # Use default value if available and value is still None
                if value is None and param.default is not param.empty:
                    value = param.default
                # Raise exception if required parameter is missing
                if value is None and param.default is param.empty:
                    raise ValueError(f"Required parameter '{name}' is missing")
                
                kwargs[name] = value
            result = await func(**kwargs) if inspect.iscoroutinefunction(func) else func(**kwargs)
        else:
            result = await func() if inspect.iscoroutinefunction(func) else func()

        return HTMLResponse(result) if isinstance(result, str) else result

    return wrapped_func
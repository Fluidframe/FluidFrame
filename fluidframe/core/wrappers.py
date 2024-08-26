import inspect, json
from typing import Callable
from starlette.requests import Request
from fluidframe.core.state import State
from starlette.responses import HTMLResponse


def html_render_wrap(func: Callable) -> HTMLResponse:
    async def wrapped_func(request: Request) -> HTMLResponse:
        sig = inspect.signature(func)
        kwargs = {}
        state = State(request)
        if sig.parameters:
            for name, param in sig.parameters.items():
                if name == 'request' or (param.annotation is Request):
                    kwargs[name] = request
                elif name == 'state' or (param.annotation is State):
                    kwargs[name]=state
                elif param.default is param.empty:
                    raise ValueError(f"Required parameter {name} is not a valid parameter either specify `request`, `state` or both as parameters")
            result = await func(**kwargs) if inspect.iscoroutinefunction(func) else func(**kwargs)
        else:
            result = await func() if inspect.iscoroutinefunction(func) else func()
        response = []

        if isinstance(result, tuple):
            for r in result:
                if isinstance(r, str):
                    response.append(r)
                elif isinstance(r, dict):
                    state_dict = r
        elif isinstance(result, str):
            response.append(result)
        elif isinstance(result, dict):
            state_dict = result
        response = HTMLResponse(''.join(response))
        if state_dict:
            retarget = state_dict.pop('HX-Retarget', None)
            if retarget:
                response.headers["HX-Target-Update"] = json.dumps(retarget)
            response.headers["X-Component-State"] = json.dumps(state_dict)
        return response

    return wrapped_func
from typing import List, Optional
from starlette.routing import Route
from fluidframe.utils import UniqueIDGenerator


class App:
    def __init__(self, title: str) -> None:
        pass


class DynamicRouter:
    def __init__(self):
        self.routes = {}

    def add_route(self, route_id, handler):
        self.routes[route_id] = Route(route_id, handler)

    def get_routes(self):
        return list(self.routes.values())
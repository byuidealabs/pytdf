from pyramid.view import (
    view_config,
    view_defaults
)
import json


@view_defaults(renderer='templates/default.pt')
class IndexView:

    def __init__(self, request):
        self.request = request

    @property
    def dependencies(self):
        with open('clientdependencies.json', 'r') as f:
            return json.load(f).items()

    @view_config(route_name='index')
    def index(self):
        return {'body': 'Hello World'}

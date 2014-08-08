from pyramid.view import (
    view_config,
    view_defaults
)


@view_defaults(renderer='templates/default.pt')
class IndexView:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='index')
    def index(self):
        return {'body': 'Hello World'}

from pyramid.view import view_config
from pyramid.response import Response


class IndexView:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='index')
    def index(self):
        return Response('<body><h1>Hello World</h1></body>')

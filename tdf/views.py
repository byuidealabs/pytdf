from pyramid.view import (
    view_config,
)
from pyramid.response import Response


class TutorialViews:

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(request):
        return Response('<body><h1>Hello World</h1></body>')

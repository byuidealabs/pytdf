from pyramid.view import (
    view_config,
    view_defaults
)
import os
import json
import glob


def _walk_paths(static_path, fmt):
    # TODO Make recursive and filter subdirectories
    cwd = os.getcwd()
    return [path.rpartition('/')[2] for path in
            glob.glob(fmt % (cwd, static_path))]


@view_defaults(renderer='templates/default.pt')
class IndexView:

    def __init__(self, request):
        self.request = request

    @property
    def dependencies(self):
        with open('clientdependencies.json', 'r') as f:
            return json.load(f).items()

    @property
    def stylesheets(self):
        static_path = self.request.static_path('tdf:public/css')
        return _walk_paths(static_path, '%s/tdf%s/*')

    @property
    def scripts(self):
        static_path = self.request.static_path('tdf:public/js')
        return _walk_paths(static_path, '%s/tdf%s/*')

    @view_config(route_name='index')
    def index(self):
        return {'body': 'Hello World'}

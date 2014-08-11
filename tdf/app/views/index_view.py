from pyramid.view import (
    view_config,
    view_defaults
)
from .base_view import BaseView


@view_defaults(renderer='templates/default.pt')
class IndexView(BaseView):
    """
    Class defining the views on the index, which, through angular, controls
    all of the front end of TDF.
    """

    def __init__(self, request):
        """
        Initializes the IndexView.

        :param request {pyramid.Request} The request object coming into the
        view.
        """
        BaseView.__init__(self, request)

    @view_config(route_name='index')
    def index(self):
        """
        Configures and loads the view specified by the route 'index'.

        :return {dict} The data to pass into the index view.
        """
        return {'body': 'Hello World'}

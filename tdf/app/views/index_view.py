from pyramid.view import (
    view_config,
    view_defaults
)
from pyramid.security import authenticated_userid
from .base_view import BaseView


@view_defaults(renderer='templates/default.pt')
class IndexView(BaseView):
    """
    Class defining the views on the index, which, through angular, controls
    all of the front end of TDF.

    Parameters
    ----------
    request : :class:`pyramid.Request`
        The request object coming into the view.
    """

    def __init__(self, request):
        BaseView.__init__(self, request)

    @view_config(route_name='index')
    def index(self):
        """
        Configures and loads the view specified by the route `index`.

        Returns
        -------
        data : dictionary
            The data to pass into the index view.
        """
        rs = {'body': 'Hello World', 'authenticated': False}
        user = authenticated_userid(self.request)
        if user is not None:
            rs['user'] = user
            rs['authenticated'] = True
        return rs

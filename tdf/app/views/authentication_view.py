"""
Defines the login and logout views used for authentication.
"""
from pyramid.view import (
    view_config,
)
from pyramid.security import (
    remember
)
from pyramid.httpexceptions import (
    HTTPFound
)

from .base_view import BaseView


class LoginView(BaseView):

    def __init__(self, request):
        BaseView.__init__(self, request)

    @view_config(route_name='login', renderer='templates/login.pt')
    def login(self):
        nxt = self.request.params.get('next') or \
            self.request.route_url('index')
        login = ''
        did_fail = False

        if 'login' in self.request.POST:
            login = self.request.POST.get('login', '')
            # psswd = self.request.POST.get('psswd', '')

            # TODO authenticate
            # if login != '':
            #    headers = remember(self.request, login)
            #    return HTTPFound(location=nxt, headers=headers)
            did_fail = True

        return {
            'login': login,
            'next': nxt,
            'failed_attempt': did_fail
        }

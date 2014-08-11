from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    print(settings)
    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth.secret'],
        hashalg='sha512'
    )
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy
    )
    config.include('pyramid_chameleon')

    config.add_static_view('public', 'tdf:public')

    # Routes
    config.add_route('index', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    # View Plugin
    config.scan('.app.views.index_view')
    config.scan('.app.views.authentication_view')

    return config.make_wsgi_app()

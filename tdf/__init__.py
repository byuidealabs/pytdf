from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    config.add_static_view('public', 'tdf:public')

    # Routes
    config.add_route('index', '/')
    config.add_route('login', '/login')

    # View Plugin
    config.scan('.app.views.index_view')
    config.scan('.app.views.authentication_view')

    return config.make_wsgi_app()

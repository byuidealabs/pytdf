from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('index', '/')
    config.scan('.app.views.index')

    config.add_static_view('public', 'public')

    return config.make_wsgi_app()

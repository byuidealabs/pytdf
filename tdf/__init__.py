from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    config.add_static_view('public', 'tdf:public')

    config.add_route('index', '/')
    config.scan('.app.views.index')

    return config.make_wsgi_app()

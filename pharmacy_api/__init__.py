"""Main entry point
"""
from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('cornice')
    config.scan('pharmacy_api.views')
    return config.make_wsgi_app()


from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from git commit -m "Remove venv directory" import DBSession, Base

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application."""
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()

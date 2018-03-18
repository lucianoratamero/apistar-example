
from apistar.backends import django_orm
from apistar.frameworks.wsgi import WSGIApp as App

from src.routes import routes
from src.auth import BasicDjangoAuthentication


settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    },
    'INSTALLED_APPS': ['src', 'django.contrib.auth', 'django.contrib.contenttypes', ],
    'AUTHENTICATION': [BasicDjangoAuthentication()],
}


app = App(
    routes=routes,
    settings=settings,
    commands=django_orm.commands,
    components=django_orm.components,
)


if __name__ == '__main__':
    app.main()

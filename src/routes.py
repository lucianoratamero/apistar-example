from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from src import views


routes = [
    Route('/', 'GET', views.welcome),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

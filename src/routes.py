from apistar import Include, Route
from apistar.handlers import docs_urls, static_urls

from src import views


routes = [
    Route('/', 'GET', views.welcome),
    Route('/criar-produto', 'POST', views.criar_produto, name='criar_produto'),
    Route('/listar-produtos', 'GET', views.listar_produtos, name='listar_produtos'),
    Route('/valida-cpf', 'POST', views.valida_cpf, name='valida_cpf'),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]


from apistar import http
from apistar.backends.django_orm import Session

from src import schemas


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def criar_produto(produto: schemas.Produto, session: Session):
    if not produto:
        return

    db_produto = session.Produto(**produto)
    db_produto.save()
    return http.Response(content=schemas.Produto(db_produto.__dict__), status=201)

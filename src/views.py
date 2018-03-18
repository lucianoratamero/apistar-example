
from apistar import http
from apistar.interfaces import Auth
from apistar.backends.django_orm import Session

from src import schemas


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def me(auth: Auth):
    return {
        "is_authenticated": auth.is_authenticated(),
        "username": auth.get_display_name(),
    }


def criar_produto(produto: schemas.Produto, session: Session):
    if not produto:
        return

    db_produto = session.Produto(**produto)
    db_produto.save()
    return http.Response(content=schemas.Produto(db_produto.__dict__), status=201)


def listar_produtos(nota: schemas.Nota, session: Session):
    produtos = session.Produto.objects.all()
    if nota is not None:
        produtos = produtos.filter(nota=nota)
    return [schemas.Produto(db_produto.__dict__) for db_produto in produtos]


def valida_cpf(cpf: schemas.CPF):
    return cpf


def criar_usuario(user: schemas.User, session: Session):
    if not user:
        return
    db_user = session.User.objects.create_user(**user)
    return schemas.User(db_user.__dict__)


def listar_usuarios(username: schemas.Username, session: Session):
    usuarios = session.User.objects.all()
    if username is not None:
        usuarios = usuarios.filter(username=username)
    return [schemas.User(db_user.__dict__) for db_user in usuarios]

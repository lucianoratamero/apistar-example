from apistar import typesystem
from apistar.exceptions import TypeSystemError
from pycpfcnpj import cpfcnpj


class Nota(typesystem.Integer):
    description = 'Nota pro produto'
    minimum = 1
    maximum = 5


class TamanhoDeProduto(typesystem.Enum):
    description = 'Acho que esse se explica'
    enum = ['pequeno', 'normal', 'grande']


class Produto(typesystem.Object):
    # Se quiser customizar, use letra minúscula (string em vez de String)
    required = ['nome', 'nota', 'tamanho']
    properties = {
        'nome': typesystem.string(description='Nome, cara. Nome.', min_length=1, max_length=100),
        'nota': Nota,
        'tamanho': TamanhoDeProduto,
    }


class CPFField(typesystem.String):
    min_length = 14
    max_length = 14
    pattern = "\d{3}\.\d{3}\.\d{3}-\d{2}"

    def __new__(cls, *args, **kwargs):
        cls.errors.update({'cpf_invalid': 'O CPF fornecido é inválido'})
        value = super().__new__(cls, *args, **kwargs)

        if not cpfcnpj.validate(value):
            raise TypeSystemError(cls=cls, code='cpf_invalid')

        return value


class CPF(typesystem.Object):
    properties = {
        'cpf': CPFField
    }


class Username(typesystem.String):
    min_length = 1


class User(typesystem.Object):
    properties = {
        'username': Username,
        'password': typesystem.String,
    }

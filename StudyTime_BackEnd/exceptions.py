class UsuarioException(Exception):
    ...

class UsuarioNotFoundError(UsuarioException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Usuário não encontrado"

class UsuarioAlreadyExistError(UsuarioException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Usuário já cadastrado"

class DisciplinaException(Exception):
    ...

class DisciplinaNotFoundError(DisciplinaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Disciplina não encontrada"

class AnotacaoException(Exception):
    ...

class AnotacaoNotFoundError(AnotacaoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Anotação não encontrada"

class TopicoException(Exception):
    ...

class TopicoNotFoundError(TopicoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Tópico não encontrado"

class TarefaException(Exception):
    ...

class TarefaNotFoundError(TarefaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Tarefa não encontrada"

class NotaException(Exception):
    ...

class NotaNotFoundError(NotaException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Nota não encontrada"

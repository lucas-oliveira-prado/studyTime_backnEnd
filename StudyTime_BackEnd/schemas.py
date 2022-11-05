from datetime import date
from pydantic import BaseModel

class DisciplinaBase(BaseModel):
    nome: str
    id_usuario: int

class DisciplinaUpdate(BaseModel):
    nome: str
    tempo_executado: int
    id_usuario: int

class AnotacaoBase(BaseModel):
    nome: str
    conteudo: str
    id_disciplina: int

class NotaBase(BaseModel):
    nota: float
    peso: float
    id_disciplina: int

class TopicoBase(BaseModel):
    tema: str
    status: int
    id_disciplina: int

class TarefaBase(BaseModel):
    titulo: str
    descricao: str
    data: date
    status: int
    id_disciplina: int

class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: str
class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str
from sqlalchemy import SmallInteger, Date, Column, ForeignKey, Integer, String, Text, Float
from database import Base

class Disciplina(Base):
    __tablename__ = 'disciplina'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    tempo_executado = Column(Integer)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)

class Anotacao(Base):
    __tablename__ = 'anotacao'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    conteudo = Column(Text(50000))
    id_disciplina = Column(Integer, ForeignKey("disciplina.id"), nullable=False)

class Nota(Base):
    __tablename__ = 'nota'
    id = Column(Integer, primary_key=True)
    nota = Column(Float)
    peso = Column(Float)
    media = Column(String(2))
    id_disciplina = Column(Integer, ForeignKey("disciplina.id"), nullable=False)

class Topico(Base):
    __tablename__ = 'topico'
    id = Column(Integer, primary_key=True)
    tema = Column(String(100))
    status = Column(SmallInteger)
    id_disciplina = Column(Integer, ForeignKey("disciplina.id"), nullable=False)

class Tarefa(Base):
    __tablename__ = 'tarefa'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descricao = Column(Text(5000))
    data = Column(Date)
    status = Column(SmallInteger)
    id_disciplina = Column(Integer, ForeignKey("disciplina.id"), nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    email = Column(String(150))
    senha = Column(String(150))






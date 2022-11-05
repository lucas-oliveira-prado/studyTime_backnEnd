from sqlalchemy.orm import Session
from sqlalchemy import and_
from exceptions import UsuarioAlreadyExistError, UsuarioNotFoundError, DisciplinaNotFoundError, AnotacaoNotFoundError, TopicoNotFoundError, TarefaNotFoundError, NotaNotFoundError
import schemas, models

########################################################
#Crud Disciplina
########################################################

def create_disciplina(db: Session, disciplina: schemas.DisciplinaBase):
    db_disciplina = models.Disciplina(**disciplina.dict())
    db.add(db_disciplina)
    db.commit() 
    db.refresh(db_disciplina)
    return db_disciplina

def get_disciplina_by_id(db: Session, disciplina_id: int):
    db_disciplina = db.query(models.Disciplina).get(disciplina_id)
    if db_disciplina is None:
        raise DisciplinaNotFoundError
    return db_disciplina

def get_all_disciplinas(db: Session, offset: int, limit: int):
    return db.query(models.Disciplina).offset(offset).limit(limit).all()

def update_disciplina(db: Session, disciplina_id: int, disciplina: schemas.DisciplinaUpdate):
    db_disciplina = get_disciplina_by_id(db, disciplina_id)
    db_disciplina.nome = disciplina.nome
    db_disciplina.tempo_executado = disciplina.tempo_executado
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina
    
def delete_disciplina_by_id(db: Session, disciplina_id: int):
    db_disciplina = get_disciplina_by_id(db, disciplina_id)
    db.delete(db_disciplina)
    db.commit()
    return

########################################################
#Crud Usuario
########################################################

def check_usuario(db: Session, usuario: schemas.UsuarioBase):
    db_usuario = db.query(models.Usuario).filter(and_(models.Usuario.email == usuario.email, models.Usuario.senha == usuario.senha)).first()
    if db_usuario is None:
        return False
    return True

def create_usuario(db: Session, usuario: schemas.UsuarioBase):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def get_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).get(usuario_id)
    if db_usuario is None:
        raise UsuarioNotFoundError
    return db_usuario

def get_all_usuario(db: Session, offset: int, limit: int):
    return db.query(models.Usuario).offset(offset).limit(limit).all()

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioBase):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db_usuario.nome = usuario.nome
    db_usuario.senha = usuario.senha
    db_usuario.email = usuario.email
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def delete_usuario_by_id(db: Session, usuario_id: int):
    db_usuario = get_usuario_by_id(db, usuario_id)
    db.delete(db_usuario)
    db.commit()
    return

########################################################
#Crud Anotação
########################################################

def create_anotacao(db: Session, anotacao: schemas.AnotacaoBase):
    db_anotacao = models.Anotacao(**anotacao.dict())
    db.add(db_anotacao)
    db.commit()
    db.refresh(db_anotacao)
    return db_anotacao

def get_anotacao_by_id(db: Session, anotacao_id: int):
    db_anotacao = db.query(models.Anotacao).get(anotacao_id)
    if db_anotacao is None:
        raise AnotacaoNotFoundError
    return db_anotacao

def get_all_anotacao(db: Session, offset: int, limit: int):
    return db.query(models.Anotacao).offset(offset).limit(limit).all()

def update_anotacao(db: Session, anotacao_id: int, anotacao: schemas.AnotacaoBase):
    db_anotacao = get_anotacao_by_id(db, anotacao_id)
    db_anotacao.nome = anotacao.nome
    db_anotacao.conteudo = anotacao.conteudo
    db.commit()
    db.refresh(db_anotacao)
    return db_anotacao

def delete_anotacao_by_id(db: Session, anotacao_id: int):
    db_anotacao = get_anotacao_by_id(db, anotacao_id)
    db.delete(db_anotacao)
    db.commit()
    return

########################################################
#Crud Topico
########################################################

def create_topico(db: Session, topico: schemas.TopicoBase):
    db_topico = models.Topico(**topico.dict())
    db.add(db_topico)
    db.commit() 
    db.refresh(db_topico)
    return db_topico

def get_topico_by_id(db: Session, topico_id: int):
    db_topico = db.query(models.Topico).get(topico_id)
    if db_topico is None:
        raise TopicoNotFoundError
    return db_topico

def get_all_topicos(db: Session, offset: int, limit: int):
    return db.query(models.Topico).offset(offset).limit(limit).all()
    
def update_topico(db: Session, topico_id: int, topico: schemas.TopicoBase):
    db_topico = get_topico_by_id(db, topico_id)
    db_topico.tema = topico.tema
    db_topico.status = topico.status
    db.commit()
    db.refresh(db_topico)
    return db_topico

def delete_topico_by_id(db: Session, topico_id: int):
    db_topico = get_topico_by_id(db, topico_id)
    db.delete(db_topico)
    db.commit()
    return
    
########################################################
#Crud Tarefa
########################################################

def create_tarefa(db: Session, tarefa: schemas.TarefaBase):
    db_tarefa = models.Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def get_tarefa_by_id(db: Session, tarefa_id: int):
    db_tarefa = db.query(models.Tarefa).get(tarefa_id)
    if db_tarefa is None:
        raise TarefaNotFoundError
    return db_tarefa

def get_all_tarefa(db: Session, offset: int, limit: int):
    return db.query(models.Tarefa).offset(offset).limit(limit).all()

def update_tarefa(db: Session, tarefa_id: int, tarefa: schemas.TarefaBase):
    db_tarefa = get_tarefa_by_id(db, tarefa_id)
    db_tarefa.titulo = tarefa.titulo
    db_tarefa.descricao = tarefa.descricao
    db_tarefa.data = tarefa.data
    db_tarefa.status = tarefa.status
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa

def delete_tarefa_by_id(db: Session, tarefa_id: int):
    db_tarefa = get_tarefa_by_id(db, tarefa_id)
    db.delete(db_tarefa)
    db.commit()
    return

########################################################
#Crud Nota
########################################################

def create_nota(db: Session, nota: schemas.NotaBase):
    db_nota = models.Nota(**nota.dict())
    db.add(db_nota)
    db.commit() 
    db.refresh(db_nota)
    return db_nota

def get_nota_by_id(db: Session, nota_id: int):
    db_nota= db.query(models.Nota).get(nota_id)
    if db_nota is None:
        raise NotaNotFoundError
    return db_nota

def get_all_notas(db: Session, offset: int, limit: int):
    return db.query(models.Topico).offset(offset).limit(limit).all()

def update_nota(db: Session, nota_id: int, nota: schemas.NotaBase):
    db_nota = get_nota_by_id(db, nota_id)
    db_nota.nota = nota.nota
    db_nota.peso = nota.peso
    db_nota.media = nota.media
    db.commit()
    db.refresh(db_nota)
    return db_nota
    
def delete_nota_by_id(db: Session, nota_id: int):
    db_nota = get_nota_by_id(db, nota_id)
    db.delete(db_nota)
    db.commit()
    return


    
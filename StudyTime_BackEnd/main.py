from fastapi import FastAPI, Body, HTTPException, Depends
from sqlalchemy.orm import Session
from exceptions import UsuarioException, DisciplinaException, AnotacaoException, TopicoException, TarefaException, NotaException
from database import get_db, engine
import crud, models, schemas
from auth.auth_handler import signJWT
from auth.auth_bearer import JWTBearer

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

########################################################
#Requisições Login e Signup
########################################################

@app.post("/login", tags=["usuario"])
async def user_login(usuario: schemas.UsuarioLoginSchema = Body(...), db: Session = Depends(get_db)):
    if crud.check_usuario(db, usuario):
        return signJWT(usuario.email)
    return {
        "error": "E-mail ou senha incorretos!"
    }

@app.post("/signup", tags=["usuario"])
async def create_usuario_signup(usuario: schemas.UsuarioBase = Body(...), db: Session = Depends(get_db)):
    try:
        crud.create_usuario(db, usuario)
        return signJWT(usuario.email)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

########################################################
#Requisições Disciplina
########################################################

@app.post("/disciplina", dependencies=[Depends(JWTBearer())])
def create_disciplina(disciplina: schemas.DisciplinaBase, db: Session = Depends(get_db)):
    crud.create_disciplina(db, disciplina)
    
@app.get("/disciplina/{disciplina_id}", dependencies=[Depends(JWTBearer())])
def get_disciplina_by_id(disciplina_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_disciplina_by_id(db, disciplina_id)
    except DisciplinaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/disciplina", dependencies=[Depends(JWTBearer())])
def get_all_disciplinas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_disciplina = crud.get_all_disciplinas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_disciplina}
    return response

@app.put("/disciplina/{disciplina_id}", dependencies=[Depends(JWTBearer())])
def update_disciplina(disciplina_id: int, disciplina: schemas.DisciplinaUpdate, db: Session = Depends(get_db)):
    try:
        return crud.update_disciplina(db, disciplina_id, disciplina)
    except DisciplinaException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/disciplina/{disciplina_id}", dependencies=[Depends(JWTBearer())])
def delete_displina_by_id(disciplina_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_disciplina_by_id(db, disciplina_id)
    except DisciplinaException as cie:
        raise HTTPException(**cie.__dict__)

########################################################
#Requisições Usuario
########################################################
    
@app.get("/usuario/{usuario_id}", dependencies=[Depends(JWTBearer())])
def get_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/usuario", dependencies=[Depends(JWTBearer())])
def get_all_usuario(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_usuario = crud.get_all_usuario(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_usuario}
    return response

@app.put("/usuario/{usuario_id}", dependencies=[Depends(JWTBearer())])
def update_usuario(usuario_id: int, usuario: schemas.UsuarioBase, db: Session = Depends(get_db)):
    try:
        return crud.update_usuario(db, usuario_id, usuario)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/usuario/{usuario_id}", dependencies=[Depends(JWTBearer())])
def delete_usuario_by_id(usuario_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_usuario_by_id(db, usuario_id)
    except UsuarioException as cie:
        raise HTTPException(**cie.__dict__)

########################################################
#Requisições Anotação
########################################################

@app.post("/anotacao", dependencies=[Depends(JWTBearer())])
def create_anotacao(anotacao: schemas.AnotacaoBase, db: Session = Depends(get_db)):
    crud.create_anotacao(db, anotacao)
    
@app.get("/anotacao/{anotacao_id}", dependencies=[Depends(JWTBearer())])
def get_anotacao_by_id(anotacao_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_anotacao_by_id(db, anotacao_id)
    except AnotacaoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/anotacao", dependencies=[Depends(JWTBearer())])
def get_all_anotacoes(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_anotacao = crud.get_all_anotacao(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_anotacao}
    return response

@app.put("/anotacao/{anotacao_id}", dependencies=[Depends(JWTBearer())])
def update_anotacao(anotacao_id: int, anotacao: schemas.AnotacaoBase, db: Session = Depends(get_db)):
    try:
        return crud.update_anotacao(db, anotacao_id, anotacao)
    except AnotacaoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/anotacao/{anotacao_id}", dependencies=[Depends(JWTBearer())])
def delete_anotacao_by_id(anotacao_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_anotacao_by_id(db, anotacao_id)
    except AnotacaoException as cie:
        raise HTTPException(**cie.__dict__)

########################################################
#Requisições Topico
########################################################

@app.post("/topico", dependencies=[Depends(JWTBearer())])
def create_topico(topico: schemas.TopicoBase = Body(...), db: Session = Depends(get_db)):
    crud.create_topico(db, topico)

@app.get("/topico/{topico_id}", dependencies=[Depends(JWTBearer())])
def get_topico_by_id(topico_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_topico_by_id(db, topico_id)
    except TopicoException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/topico", dependencies=[Depends(JWTBearer())])
def get_all_topicos(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_topico = crud.get_all_topicos(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_topico}
    return response

@app.put("/topico/{topico_id}", dependencies=[Depends(JWTBearer())])
def update_topico(topico_id: int, topico: schemas.TopicoBase, db: Session = Depends(get_db)):
    try:
        return crud.update_topico(db, topico_id, topico)
    except TopicoException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/topico/{topico_id}", dependencies=[Depends(JWTBearer())])
def delete_topico_by_id(topico_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_topico_by_id(db, topico_id)
    except DisciplinaException as cie:
        raise HTTPException(**cie.__dict__)
        
########################################################
#Requisições Tarefas
########################################################

@app.post("/tarefa", dependencies=[Depends(JWTBearer())])
def create_tarefa(tarefas: schemas.TarefaBase, db: Session = Depends(get_db)):
    crud.create_tarefa(db, tarefas)
    
@app.get("/tarefa/{tarefa_id}", dependencies=[Depends(JWTBearer())])
def get_tarefa_by_id(tarefa_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_tarefa_by_id(db, tarefa_id)
    except TarefaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/tarefa", dependencies=[Depends(JWTBearer())])
def get_all_tarefas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_tarefa = crud.get_all_tarefa(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_tarefa}
    return response

@app.put("/tarefa/{tarefa_id}", dependencies=[Depends(JWTBearer())])
def update_tarefa(tarefa_id: int, tarefa: schemas.AnotacaoBase, db: Session = Depends(get_db)):
    try:
        return crud.update_tarefa(db, tarefa_id, tarefa)
    except TarefaException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/tarefa/{tarefa_id}", dependencies=[Depends(JWTBearer())])
def delete_tarefa_by_id(tarefa_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_tarefa_by_id(db, tarefa_id)
    except TarefaException as cie:
        raise HTTPException(**cie.__dict__)

########################################################
#Requisições Notas
########################################################

@app.post("/nota", dependencies=[Depends(JWTBearer())])
def create_nota(nota: schemas.NotaBase, db: Session = Depends(get_db)):
    crud.create_nota(db, nota)
    
@app.get("/nota/{nota_id}", dependencies=[Depends(JWTBearer())])
def get_nota_by_id(nota_id: int, db: Session = Depends(get_db)):
    try:
        return crud.get_nota_by_id(db, nota_id)
    except NotaException as cie:
        raise HTTPException(**cie.__dict__)

@app.get("/nota", dependencies=[Depends(JWTBearer())])
def get_all_notas(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    db_nota = crud.get_all_notas(db, offset, limit)
    response = {"limit": limit, "offset": offset, "data": db_nota}
    return response

@app.put("/nota/{nota_id}", dependencies=[Depends(JWTBearer())])
def update_nota(nota_id: int, nota: schemas.NotaBase, db: Session = Depends(get_db)):
    try:
        return crud.update_nota(db, nota_id, nota)
    except NotaException as cie:
        raise HTTPException(**cie.__dict__)

@app.delete("/nota/{nota_id}", dependencies=[Depends(JWTBearer())])
def delete_nota_by_id(nota_id: int, db: Session = Depends(get_db)):
    try:
        return crud.delete_nota_by_id(db, nota_id)
    except NotaException as cie:
        raise HTTPException(**cie.__dict__)



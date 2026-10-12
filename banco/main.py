import sqlite3
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

banco = sqlite3.connect("disciplinas.db")
cursor = banco.cursor()

def create_table():
    cursor.execute("CREATE TABLE disciplinas(id_cod_disciplina string primary key NOT NULL, nome string NOT NULL, periodo string, nota integer, frequencia string, professor string)")
    banco.commit()

@app.get("/disciplinas/")
def read():
    banco = sqlite3.connect("disciplinas.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM disciplinas")
    resposta = cursor.fetchall()
    banco.close()
    return resposta

@app.post("/disciplinas/")
def cadastrar(
    cod:Annotated[str, Form()], 
    nome:Annotated[str, Form()], 
    periodo:Annotated[str, Form()], 
    nota:Annotated[float, Form()],
    frequencia:Annotated[str, Form()], 
    professor:Annotated[str, Form()] 
    ):

    banco = sqlite3.connect("disciplinas.db")
    cursor = banco.cursor()
    cursor.execute("""INSERT INTO disciplinas VALUES (:cod, :nome, :periodo, :nota, :frequencia, :professor) """,
    {
        "cod": cod,
        "nome": nome,
        "periodo": periodo,
        "nota": nota, 
        "frequencia": frequencia, 
        "professor": professor
    })
    banco.commit()
    banco.close()
    return {"message":"Disciplina cadastrada com sucesso!"}


#create_table()
#cadastrar('arq001', 'arquitetura', '2026.2', 9, '85%', 'Giovani')

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API de Atendimento Automático"}

@app.get("/atendimento")
def atendimento(problema: str):

    return {"problema_recebido": problema}

from fastapi import FastAPI, Request
import requests

app = FastAPI()


TOKEN = "usn1rkwqyr2oe1ie"
INSTANCE = "instance176843"


menu = """ 
Escolha o número do setor relacionado ao seu problema: 

1 - Cartões
2 - Conta Corrente
3 - Contratos de Seguros 
4 - Seguros
5 - Investimentos
6 - Fraude/Travas de Segurança
7 - Consignados
8 - Consórcios
9 - Financiamento Veicular
10 - Financiamento Imobiliário
11 - Desacordo Comercial
12 - Acordos
13 - Câmbio

"""

@app.get("/")
def home():

    return {"mensagem": menu}

@app.post("/wehook")
async def webhook(request:Request):

    dados = await request.json()

    mensagem = dados.get("body")
    numero = dados.get("from")

    if mensagem == "1":

        resposta = "Você foi direcionado para o setor de Cartões."
    
    elif mensagem == "2": 
        
        resposta = "Você foi direcionado para o setor de Conta Corrente."
        
    elif mensagem == "3": 
         
        resposta = "Você foi direcionado para o setor de Contratos de Seguros."
       
    elif mensagem == "4": 
          
        resposta = "Você foi direcionado para o setor de Seguros."
    
    elif mensagem == "5": 
           
        resposta = "Você foi direcionado para o setor de Investimentos."
    
    elif mensagem == "6": 
            
        resposta = "Você foi direcionado para o setor de Fraude/Travas de Segurança."
    
    elif mensagem == "7": 
        
        resposta = "Você foi direcionado para o setor de Consignados."
       
    elif mensagem == "8": 
        
        resposta = "Você foi direcionado para o setor de Consórcios."
        
    elif mensagem == "9": 
        
        resposta = "Você foi direcionado para o setor de Financiamento Veicular."
       
    elif mensagem == "10": 
        
        resposta = "Você foi direcionado para o setor de Financiamento Imobiliário."
       
    elif mensagem == "11": 
       
        resposta = "Você foi direcionado para o setor de Desacordo Comercial."
        
    elif mensagem == "12": 
        
        resposta = "Você foi direcionado para o setor de Acordos."
     
    elif mensagem == "13": 
        resposta = "Você foi direcionado para o setor de Câmbio."
    
    else:
        resposta = menu
  
  
requests.post(f"https://api.ultramsg.com/instance176843/messages/chat",
    data={
        "token": "usn1rkwqyr2oe1ie",
        "to": numero,
        "body": resposta
    }

)
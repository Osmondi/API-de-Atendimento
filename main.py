from fastapi import FastAPI
import requests

app = FastAPI()

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


@app.get("/enviar")
def enviar():

    requests.post(
        "https://api.ultramsg.com/instance176843/messages/chat",  
        data={"token": "usn1rkwqyr2oe1ie",
              "to": "5521967602311",
              "body": "Olá, teste da API"
    }
    )

    return{"mensagem": "Mensagem Enviada"}

@app.get("/atendimento")
def atendimento(opcao: str):

    if opcao == "1": 
        return {
            "setor": "Cartões",
            "mensagem": "Você foi direcionado para o setor de Cartões."
        }
    
    elif opcao == "2": 
        return {
            "setor": "Conta Corrente",
            "mensagem": "Você foi direcionado para o setor de Conta Corrente."
        }
    
    elif opcao == "3": 
        return {
            "setor": "Contratos de Seguros",
            "mensagem": "Você foi direcionado para o setor de Contratos de Seguros."
        }
    
    elif opcao == "4": 
        return {
            "setor": "Seguros",
            "mensagem": "Você foi direcionado para o setor de Seguros."
        }
    
    elif opcao == "5": 
        return {
            "setor": "Investimentos",
            "mensagem": "Você foi direcionado para o setor de Investimentos."
        }
    
    elif opcao == "6": 
        return {
            "setor": "Fraude/Travas de Segurança",
            "mensagem": "Você foi direcionado para o setor de Fraude/Travas de Segurança."
        }
    
    elif opcao == "7": 
        return {
            "setor": "Consignados",
            "mensagem": "Você foi direcionado para o setor de Consignados."
        }
    
    elif opcao == "8": 
        return {
            "setor": "Consórcios",
            "mensagem": "Você foi direcionado para o setor de Consórcios."
        }
    
    elif opcao == "9": 
        return {
            "setor": "Financiamento Veicular",
            "mensagem": "Você foi direcionado para o setor de Financiamento Veicular."
        }
    
    elif opcao == "10": 
        return {
            "setor": "Financiamento Imobiliário",
            "mensagem": "Você foi direcionado para o setor de Financiamento Imobiliário."
        }
    
    elif opcao == "11": 
        return {
            "setor": "Desacordo Comercial",
            "mensagem": "Você foi direcionado para o setor de Desacordo Comercial."
        }
    
    elif opcao == "12": 
        return {
            "setor": "Acordos",
            "mensagem": "Você foi direcionado para o setor de Acordos."
        }
    
    elif opcao == "13": 
        return {
            "setor": "Câmbio",
            "mensagem": "Você foi direcionado para o setor de Câmbio."
        }

    else:
        return {
             "erro": "Opção inválida",
             "mensagem": menu
        }

@app.post("/webhook")
def webhook():

    return {
        "mensagem": "Webhook funcionando"
    }
from dotenv import load_dotenv
import os
load_dotenv(override=True)

def create_credentials() -> dict:
    #Cria o dicionario do arquivo credenciais do google sheets api
    return {"installed":{"client_id":os.getenv("CLIENT_ID"),
                  "project_id":os.getenv("PROJECT_ID"),
                  "auth_uri":"https://accounts.google.com/o/oauth2/auth",
                  "token_uri":"https://oauth2.googleapis.com/token",
                  "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
                  "client_secret":os.getenv("REDIRECT_URIS"),"redirect_uris":["http://localhost"]}}

def create_token() -> dict:
    #Cria o dicionario do arquivo token do google sheets api
    return {"token":os.getenv('ACCESS_TOKEN'), 
        "refresh_token":os.getenv('REFRESH_TOKEN'), 
        "token_uri": "https://oauth2.googleapis.com/token", 
        "client_id": os.getenv('CLIENT_ID'), 
        "client_secret": os.getenv('CLIENT_SECRET'), "scopes": ["https://www.googleapis.com/auth/spreadsheets"], 
        "universe_domain": "googleapis.com", "account": "", "expiry": "2024-12-23T16:46:42.974405Z"}
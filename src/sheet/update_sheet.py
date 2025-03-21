from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sheet.create_tokens import create_credentials,create_token
import pandas as pd

def update_sheets(Id_tabela:str, nome_tabela:str, df:pd.DataFrame) -> pd.DataFrame | None:
    # Atualiza a Planilha em questão
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    SAMPLE_SPREADSHEET_ID = Id_tabela
    creds = None

    try:
        # Pega as credenciais do token.json (simulado com a função)
        token_data = create_token()
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)

        # Se o token não for válido, tenta renovar ou recria pelo fluxo
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                credential_data = create_credentials()
                flow = InstalledAppFlow.from_client_config(credential_data, SCOPES)
                creds = flow.run_local_server(port=0)
                # Aqui você poderia persistir esse novo token se quiser

        # Constrói o serviço de API do Sheets
        service = build("sheets", "v4", credentials=creds)

        # Prepara os dados que serão enviados para o Google Sheets
        body = {
            "values": [df.columns.values.tolist()] + df.values.tolist()
        }

        # Faz o update no Google Sheets
        sheet = service.spreadsheets()
        result = sheet.values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=nome_tabela,
            valueInputOption="USER_ENTERED",  # Pode ser RAW ou USER_ENTERED
            body=body
        ).execute()
        return result

    except HttpError as err:
        print(f"Ocorreu um erro ao atualizar o Google Sheets: {err}")
        return None
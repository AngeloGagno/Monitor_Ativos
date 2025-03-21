import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sheet.create_tokens import create_credentials,create_token

def get_sheets(Id_tabela:str,tamanho_tabela:str) -> pd.DataFrame | None:
    # Recebe a planilha em questão
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    SAMPLE_SPREADSHEET_ID = Id_tabela
    SAMPLE_RANGE_NAME = tamanho_tabela
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

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
        df =result['values'][1:]
        header = result['values'][0]
        return pd.DataFrame(df,columns=header)
    
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    print(get_sheets('1Cko4FCTmjDhg6uNe2s7xOZcTG1es1DvVg6iGOlfNlGA','airbnb!A:F'))
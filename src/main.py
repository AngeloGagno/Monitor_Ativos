from request.get_status import Check_Activity
from sheet.get_sheet import get_sheets
from sheet.update_sheet import update_sheets
import os
from dotenv import load_dotenv
def main() -> None:
    load_dotenv(override=True)
    sheet_id = os.getenv('SHEETS_ID')
    sheet = get_sheets(sheet_id,'airbnb!A:F')
    update_sheets(sheet_id,'airbnb',Check_Activity(sheet).dataframe())

if __name__ == '__main__':
    main()

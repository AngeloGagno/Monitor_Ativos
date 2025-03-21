import requests
import pandas as pd

class Check_Activity:
    def __init__(self,df:pd.DataFrame) -> bool:
        self.df = df
        self.check_link = self.check_link()
        
    def check_active(self,link:str):
        status_code = requests.get(link).status_code
        if status_code in [400,404,410]:
            return False
        return True
    
    def check_link(self) -> pd.DataFrame:
        for i in range(0,len(self.df)):
            link = self.df.loc[i,'Link']
            if link:
                self.df.loc[i,'Status'] = self.check_active(link)
        return self.df
    
    def dataframe(self) -> pd.DataFrame:
        return self.check_link
    
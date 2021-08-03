import pandas as pd

class HotelsInfo:
    def __init__(self):
        self.dfColumns = ['nome', 'diaria', 'municipio', 'avaliacoes', 'data']
        self.hotels = pd.DataFrame(columns=self.dfColumns)
    
    def add(self, name, value, city, reviews, date):
        self.hotels = self.hotels.append({'nome': name, 'diaria': value, 'municipio': city, 'avaliacoes':reviews, 'data':date}, ignore_index= True)
    
    def finish(self, date):
        self.hotels.to_excel("HoteisMT_"+date+".xlsx")
        
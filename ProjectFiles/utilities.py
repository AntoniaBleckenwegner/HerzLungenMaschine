# Import external packages

from multiprocessing.connection import wait
import pandas as pd
from datetime import datetime
import numpy as np
import re




# Classes 

class Subject():
    def __init__(self, file_name):

        ### Aufgabe 1: Interpolation ###

        __f = open(file_name)
        self.subject_data = pd.read_csv(__f)
        self.subject_data = self.subject_data.interpolate(method='quadratic', axis=0)
        __splited_id = re.findall(r'\d+',file_name)      
        self.subject_id = ''.join(__splited_id)
        self.names = self.subject_data.columns.values.tolist()
        self.time = self.subject_data["Time (s)"]        
        self.spO2 = self.subject_data["SpO2 (%)"]
        self.temp = self.subject_data["Temp (C)"]
        self.blood_flow = self.subject_data["Blood Flow (ml/s)"]
        print('Subject ' + self.subject_id + ' initialized')
        
    



## Aufgabe 2: CMA/SMA 2 verschiedene Versuche
   # def calculate_CMA(df,n):
        #bloodflow  = df["Blood Flow (ml/s)"].to_frame()
      #  bloodflow['CMA'] = bloodflow["Blood Flow (ml/s)"].expanding().mean()
      #  return bloodflow
    
   # def calculate_SMA(df,n):
       # bloodflow  = df["Blood Flow (ml/s)"].to_frame()
      #  bloodflow['SMA'] = bloodflow["Blood Flow (ml/s)"].rolling(n).mean()
       # return bloodflow
 
def calculate_CMA(df,n):
    return df.expanding(n).mean()
    

def calculate_SMA(df,n):
    return df.rolling(n).mean()




# Aufgabe 4
# 4.1 Der Simple Moving Average ist Sinnvoll bei rauschenden Signalen und kurzen Außreißern
# Vorteile:
#   -geglätteter Chart
#   -Erkennen von Trends bzw. Trendwende
#   -va. für Charts mit höhrer Timeframe

# Nachteile:
#   -ungeeignet wenn Echtzeit Signale benötigt werden (zB bei HLM soll schnell auf abnormale Werte reagiert werden)
#   -Außreiser nicht sichtbar (zB bei manchen Preischarts doch von großer Relvanz (vgl. Depeg Stablecoin))




        

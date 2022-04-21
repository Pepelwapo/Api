from operator import index
import requests
import pandas as pd
import numpy as np


#response=requests.get('https://v2.zplayer.live/api/account/info?key=305x06jm5uwtuxf2pe1')
#response=requests.get('https://v2.zplayer.live/api/folder/list?key=305x06jm5uwtuxf2pe1')
#response=requests.get('https://v2.zplayer.live/api/file/list?key=305x06jm5uwtuxf2pe1')

response=requests.get('https://v2.zplayer.live/api/folder/list?key=305x06jm5uwtuxf2pe1')
df1=pd.read_json(response.content)

ddf=pd.read_json(df1)

ddf=ddf['result']
ddf=ddf.loc[:'files']


df=pd.DataFrame(ddf)
#Quitar parentesis para poder separar por columnas y ser legible
splittest=df['result'].str.split(',',expand=True)

#abriendo archivo

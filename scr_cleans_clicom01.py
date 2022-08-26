import os
import pandas as pd
import numpy as np
import csv
import lib.alcalib as ac

ac.write_log('scr_cleans_clicom01.py','--','--','--')
# leggo file csv saltando prima riga di legenda
df = pd.read_csv(r'C:\alca\data\crmtran.csv',header=None,skiprows=1)
numfields=df.shape[1]
df1 = df.loc[:,1:]
df2 = df1.apply(pd.to_numeric, errors='coerce')
df3 = df2.fillna(df2.mean())
df4= np.round(df3,decimals=2)
null_cols = df4.columns[df4.isnull().all()]
df4.drop(null_cols, axis = 1, inplace = True)

with open(r'C:\alca\data\cleancrmtran.csv', 'w') as fw:
    strih='indice,fatt,redd,perc,util,pag,codice\n'
    fw.write(strih)
    for idx,row in enumerate(df4.itertuples()):
        stri1=str(row[0])+','+ str(row[1])+','+str(row[2])+','+str(row[3])+','+ str(row[4])+','  \
              +str(row[5])+','+ df.iat[idx,0] +'\n'
        fw.write(stri1)
    ac.write_log('scr_cleans_clicom01.py', 'ope:righe scritte:'+str(idx), '--', '--')
fw.close()

dff = pd.read_csv(r'C:\alca\data\cleancrmtran.csv',header=None,skiprows=1)
numfields=dff.shape[1]
dff1 = dff.loc[:,1:]
print(dff1)


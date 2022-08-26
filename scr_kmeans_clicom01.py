import os
import pandas as pd
from sklearn.cluster import KMeans
import csv

import lib.alcalib as ac

ac.write_log('scr_kmeans_clicom01.py','--','--','--')
#df1 = pd.read_csv(r'C:\xampp\htdocs\alca\upload\cleanclicom.csv',header=None,skiprows=1)
dfini = pd.read_csv(r'C:\alca\data\clicom.csv',header=None,skiprows=1)
df1 = pd.read_csv(r'C:\alca\data\cleanclicom.csv',header=None,skiprows=0)
df = df1.loc[:,1:100]
kmeans = KMeans(17).fit(df)

cc = kmeans.labels_
centroids = kmeans.cluster_centers_
print('id_centroid, x    ,    y')
for i, c in enumerate(centroids):
	print(f'{i}--     {round(c[0], 2)}--    {round(c[1], 2)} --  {round(c[2], 2)}  --  {round(c[3], 2)}   --{round(c[4], 2)}')
labels = kmeans.labels_
ff=df1.to_numpy()
fflen=len(ff[0])
result = zip(ff , kmeans.labels_)
sortedR = sorted(result, key=lambda x: x[1])
stri=''
with open(r'C:\alca\data\clustclicom.csv', 'w', encoding='utf-8') as fw:
    for i in sortedR:
        for x in range(0,fflen,1):
            stri=stri + str(i[0][x]) +','
        ff = int(i[0][0])
        cc = dfini.iloc[ff][0]
        fw.write(str(cc)+','+stri+ str(i[1]))
        fw.write('\n')
        stri=''
fw.close()

print('codcli, valori feature    , id-centroid')
for el in sortedR:
    aa=el
    codcli=el[0][0]
    val_feat=el[0][1]
    val_feat=el[0][1:12]
    id_centroid=el[1]

    print(codcli,val_feat,id_centroid)

with open(r'C:\alca\data\clicom_clustered.csv', 'w', encoding='utf-8') as fw:
    writer = csv.writer(fw, lineterminator='\n')
    for el in sortedR:
        aa = el
        codcli = el[0][0]
        val_feat1 = el[0][1]
        val_feat = el[0][1:12]
        id_centroid = el[1]
        fw.write(str(codcli) +','+ str(val_feat)+','+ str(id_centroid) +'\n')
import pandas as pd

sc = pd.read_csv('out/score.sc', sep=r' +') 
sc['sample'] = sc['description'].str[:-5]

data = pd.read_csv('out/alex.csv')

sc = sc.set_index('sample')
data = data.set_index('sample')

j = data.join(sc)
j.to_csv('joined.csv')

print(j.head())

import pandas
import math

def f(x):
  return math.log(x+10, 10) # log of x+10, base 10

df = pandas.read_csv('data.csv')
df['log kcat'] = df['kcat'].apply(f)
df['log km'] = df['km'].apply(f)

df2 = pandas.DataFrame() 

df2['sample'] = df['sample']
df2['kcat'] = df['log kcat']
df2['km'] = df['log km']
df2['eff'] = df['linear_slope']
df2['seq'] = df['seq']

df2.to_csv('data2.csv')

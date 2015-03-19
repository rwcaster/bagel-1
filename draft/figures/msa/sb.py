import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fig, axes = plt.subplots( nrows=1, ncols=1, figsize=(9, 22) )
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

df = pd.read_csv( 'sb_data.csv' )
df = df.drop('sample', axis=1) 


fig.savefig( 'sb_heatmap.pdf' )
plt.close() 


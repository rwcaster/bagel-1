import pandas
from matplotlib.pyplot import savefig 
df = pandas.read_csv( 'yields.txt' )
df['yield2'] = df['yield'] - df['yield'].min() 
df.hist() 
savefig( 'yields.pdf' ) 

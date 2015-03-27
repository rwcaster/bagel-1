import pandas
import glob 
all_scores = pandas.DataFrame() 
for sf in glob.glob( '*sc' ):
  df = pandas.read_csv( sf , sep=r'\s+', header=0 ) 
  all_scores = all_scores.append( df ) 

all_scores.to_csv( 'all.sc' ) 
 

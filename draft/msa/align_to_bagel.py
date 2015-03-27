import argparse 
import re

parser = argparse.ArgumentParser()
parser.add_argument('msa')
args = parser.parse_args()

with open(args.msa) as msa:
  msa = msa.readlines()

bgl = msa[1] # second line in file 
others = msa[2:] 
numbers = [ i for i, j in enumerate( bgl ) if re.match( r'[a-z]', j ) ] 

for line in msa:
  if line.startswith(r'>'):
    print( line.strip() ) 
  else:
    alignment = [ j for i, j in enumerate( list( line ) ) if i in numbers ] 
    print( ''.join( alignment ) )



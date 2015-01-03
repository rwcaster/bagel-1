from pdb import pose
from pandas import read_csv

csv = read_csv('ascan.csv')
csv.set_index('seq') 
mypose = pose.PDB('wt.pdb')

for atom in mypose.allatm:
  try:
    tmp = csv[(csv['seq'] == atom.seq)]
    atom.bfactor = float(tmp['normalized kcat'])
  except:
    atom.bfactor = 0.0
  print(atom)

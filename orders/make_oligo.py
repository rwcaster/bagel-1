from core.db.amino_acid import aa, ecoli_codon, rc
from sys import argv
import re

if len(argv) < 3: 
  print("usage: python makeoligo.py <fasta> <list>")
  exit()

with open(argv[1], 'r') as f:
  gene = f.readlines()[0].strip() 

with open(argv[2], 'r') as l:
  lis = [ i.strip() for i in l.readlines() if i != '\n' ]

for line in lis:
  seq = [gene[i:i+3] for i in range(0, len(gene), 3)]
  l = []
  switches = re.split(r'\+', line)
  for switch in switches:
    old = switch[0]
    i = int(''.join( switch[ 1:-1] ))
    new = switch[-1]
    ori = aa[seq[i-1]]
    if old is ori:
      seq[i-1] = ecoli_codon[new].upper()
      l += [i]
    else :
      e = 'error: you say ' + old + ' but seq has ' + ori
      break
  if l:
    e = rc(''.join(seq[min(l)-6:max(l)+4]))
    e = re.sub(r'([atcg]{15})[atcg]{0,}([atcg]{15})', r'\1,\2', e)
  print '+'.join(switches) + ',' + e


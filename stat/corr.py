from ct import aa, cod, one, rc
from sys import argv
import re

# master.csv
# with open(argv[1], 'r') as f:
  # master = f.readlines()

# score.sc
with open(argv[1], 'r') as l:
  lis = l.read().lower()
  lis = re.sub(r'[A-Za-z]{3}', one, lis)
  print(lis)


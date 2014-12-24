from pdb import pose
from numpy import log
from random import random 
from pandas import read_csv

csv = read_csv('out.csv')
csv['seq'] = csv['sample'].str.replace(r'[a-z]', '')
csv['newaa'] = csv['sample'].str[-1]
csv['oldaa'] = csv['sample'].str[0]

# calc kcat/km
csv['eff'] = csv['kcat'] / csv['km'] 
csv['err3'] = csv['eff'] * ((csv['err1']/csv['kcat'])**2+(csv['err2']/csv['km'])**2)**0.5

# calc % errs
csv['%err1'] = csv['err1']/csv['kcat']
csv['%err2'] = csv['err2']/csv['km']
csv['%err3'] = csv['err3']/csv['eff']

# logs and normalized logs
csv['log kcat'] = log(csv['kcat']+1)
csv['log km'] = log(csv['km']+1)
csv['log eff'] = log(csv['eff']+1)
csv['normalized kcat'] = csv['log kcat'] / max(csv['log kcat'])
csv['normalized km'] = csv['log km'] / max(csv['log km'])
csv['normalized eff'] = csv['log eff'] / max(csv['log eff'])

csv.to_csv('all.csv') #dump all results

min_yield = 0.165 
csv[(csv['yield'] < min_yield )].to_csv('noy.csv') # dump non-yielding
csv = csv[(csv['yield'] > min_yield )] # filter these out
csv[(csv['newaa'] == 'a')].to_csv('ascan.csv') # dump ascan
csv = csv[(csv['newaa'] != 'a')] # filter out 
csv.to_csv('desi.csv') # dump the designed mutations

# analyzes the output from process.py

from pdb import pose
from numpy import log
from random import random 
from pandas import read_csv

csv = read_csv('out/raw_out.csv')

# metadata 
csv['seq'] = csv['sample'].str.replace(r'[a-z]', '')
csv['newaa'] = csv['sample'].str[-1]
csv['oldaa'] = csv['sample'].str[0]

min_yield = 0.165 # cutoff for expressed
csv[(csv['yield'] < min_yield )].to_csv('out/noy.csv') # dump non-yielding
csv = csv[(csv['yield'] > min_yield)] # filter these out right away 

min_r = 0.95 # cutoff for linear
csv[(csv['R'] > min_r )].to_csv('out/linear-only.csv') # dump non-yielding
csv = csv[(csv['R'] < min_r)] # filter these out right away 

# calc kcat/km for remainder
csv['eff'] = csv['kcat'] / csv['km'] 
csv['err3'] = csv['eff'] * ((csv['err1']/csv['kcat'])**2+(csv['err2']/csv['km'])**2)**0.5

# calc % errs
csv['%err1'] = csv['err1']/csv['kcat']
csv['%err2'] = csv['err2']/csv['km']
csv['%err3'] = csv['err3']/csv['eff'] 

min_err1 = min_err2 = min_err3 = 0.25 #cutoff
csv = csv[(csv['yield'] > min_yield) & (csv['%err1'] < min_err1) & (csv['%err2'] < min_err2) & (csv['%err3'] < min_err3)] # filter out high errors 
csv[(csv['yield'] > min_yield) & (csv['%err1'] > min_err1) & (csv['%err2'] > min_err2) & (csv['%err3'] > min_err3)].to_csv('high-error.csv') # filter out high errors 

# logs and normalized logs
csv['log kcat'] = log(csv['kcat']+1)
csv['log km'] = log(csv['km']+1)
csv['log eff'] = log(csv['eff']+1)
csv['normalized kcat'] = csv['log kcat'] / max(csv['log kcat'])
csv['normalized km'] = csv['log km'] / max(csv['log km'])
csv['normalized eff'] = csv['log eff'] / max(csv['log eff'])

csv.to_csv('out/all-expressed.csv') #dump all results

csv.to_csv('out/all-low-error.csv')

csv[(csv['newaa'] == 'a')].to_csv('out/ascan.csv') # dump ascan
csv = csv[(csv['newaa'] != 'a')] # filter out 

csv.to_csv('out/designs.csv') # dump the designed mutations

import pandas
import argparse 
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy import arange 
from numpy import linspace 

# special import of matplotlib 
# do this before importing pylab or pyplot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import StringIO

parser = argparse.ArgumentParser()
parser.add_argument( 'input_csv' )
parser.add_argument( 'output_csv' ) 
parser.add_argument( 'plot_path', help='Path of directory to hold output plots' )
args = parser.parse_args()
 
def mm(S, kcat, km): return kcat*S/(km+S)
def si(S, kcat, km, ki): return kcat*S/(km+S*(1+S/ki))
def f(m, x, b): return m*x+b

c = 0.25 # cutoff for errors 
 
def fit(data):
  '''
  Does linear, Michaelis-Menten, and Michaelis-Menten with substrate inhibition
  fits with error checking, and makes diagnostic plots 

  example usage as a module:

    from core import fit 
    grouped = df.groupby( 'sample' ).apply( fit ) 

  example usage as a standalone script:

    python analyze_data.py data.csv data_out.csv plots/ 
  '''

  # try all the fits 

  # linear params
  slope, intercept, r_value, p_value, std_err = linregress(data['s'], data['kobs'])
  
  # michaelis menten params
  p0 = ( data['kobs'].max(), data['s'].mean() )
  (kcat, km), cov = curve_fit(mm, data['s'], data['kobs'], p0=p0) 
  err1, err2 = [ abs(cov[i][i])**0.5 for i in range(2) ]
  
  # substrate inhibition params
  try:
    p0 = ( data['kobs'].max(), data['s'].mean(), data['s'].mean() )
    (si_kcat, si_km, ki), si_cov = curve_fit(si, data['s'], data['kobs'], p0=p0)
    err4, err5, err_ki = [ abs(si_cov[i][i])**0.5 for i in range(3) ]
    if ki and err_ki/ki > c:
      err_ki = ki = None
  except:
    ki = err_ki = None

  # set up plot 
  name = data.sample.values[0] 
  fig, ax = plt.subplots( nrows=1, ncols=1 )
  ax.scatter( data.s, data.kobs )
  ax.set_title( name.upper() )
  ax.set_xlabel( r'$\mathregular{ 4-nitrophenyl-\beta-D-glucoside}$ (M)' ) 
  ax.set_ylabel( r'Rate observed $\mathregular{(min^{-1}) }$' )
  x = linspace( 0, data.s.max() ) 

  # error checking 
  if err1/kcat < c and err2/km < c: #mm errors OK 
    eff = kcat / km 
    err3 = eff*((err1/kcat)**2 + (err2/km)**2)**0.5

    # check for good ki fit and make ki plot if necessary 
    if ki and err_ki/ki < 0.1:
      # make MM + substrate inhibition plot! 
      y = [ si(xx, kcat, km, ki ) for xx in x ]
      ax.plot( x, y ) 

    else: # ki error is too high
      # make Michaelis-Menten plot! 
      y = [ mm(xx,kcat,km) for xx in x ]
      ax.plot( x, y ) 

  elif err1/kcat > c or err2/km > c: #mm errors too high
    kcat = err1 = km = err2 = None
    eff, err3 = slope, std_err

    # maken ze linear plot 
    y = [ f(slope,xx,intercept) for xx in x ]
    ax.plot( x, y ) 

  else:
    # no maken ze plot 
    kcat = km = err1 = err2 = err3 = eff = None

  fig.savefig( "%s/%s.png" % ( args.plot_path, name ) )
  plt.close(fig)

  result = { 
    'yield': '%1.2f' % data['yield'].mean(), 
    'seq': str( data.sample.values[0] )[1:-1], 
    'kcat': kcat, 'err_kcat': err1, 
    'km': km, 'err_km': err2, 
    'kcat/km': eff, 'err_kcat/km': err3, 
    'ki': ki, 'err_ki': err_ki, 
  }
    
  return pandas.Series(result)
 
# io
plates = pandas.read_csv( args.input_csv ) 
fits = plates.groupby( by='sample' ).apply( fit )
fits.to_csv( args.output_csv ) 


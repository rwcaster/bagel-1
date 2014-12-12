import pandas
from scipy.optimize import curve_fit
from scipy.stats import linregress
from numpy import linspace
import matplotlib as plt

def mm(S, kcat, km): return kcat*S/(km+S)
def si(S, kcat, km, ki): return kcat*S/(km+S*(1+S/ki))
def f(m, x, b): return m*x+b

def fit(data):
    slope, intercept, r_value, p_value, std_err = linregress(data['S'], data['kobs'])
    
    (kcat, km), cov = curve_fit( mm, data['S'], data['kobs'], p0=(data['kobs'].max(),data['S'].mean()) )
    err1, err2 = [ abs(cov[i][i])**0.5 for i in range(2) ]
    
    #p0=(data['kobs'].max(),data['S'].mean(),data['S'].mean())
    #(si_kcat, si_km, ki), si_cov = curve_fit( si, data['S'], data['kobs'], p0=p0)
    #err1, err2, err4 = [ abs(si_cov[i][i])**0.5 for i in range(3) ]

    mm_x = lm_x = si_x = linspace(0,max(data['S']))
    mm_y = [mm(xx,kcat,km) for xx in mm_x]
    #si_y = [si(xx,si_kcat,si_km,ki) for xx in si_x]
    lm_y = [f(slope,xx,intercept) for xx in lm_x]
    
    eff, err3 = (kcat/km, kcat/km*(err1/kcat)**2+(err2/km)**2)
            
    result = { 
        'sample': data['Sample'].iget(0),
        'yield': data['Yield'].iget(0),
        'x': data['S'].tolist(), 
        'y': data['kobs'], 

        'kcat': kcat, 
        'err1': err1, 
        'km': km, 
        'err2': err2, 
        'eff': eff, 
        'err3': err3,

        'slope': slope,
        'std_err': std_err, 
        'R': r_value,

        'mm_x': mm_x, 
        'mm_y': mm_y,
        'lm_x': lm_x, 
        'lm_y': lm_y,
        #'si_x': si_x, 
        #'si_y': si_y,
    }
    return pandas.Series(result)

plates = pandas.read_csv('plates.csv')
fits = plates.groupby(by='Sample').apply(fit)
fits.to_csv("out.csv")

#for sample, fit in fits.iterrows():
#    plt.figure(figsize=(16,4))
#    plt.subplot(131)
#    plt.scatter(fit['x'], fit['y'])
#    plt.title("Sample=%s\nYield=%1.2f mg/mL" % (sample, fit['yield']))
#    plt.xlabel('4-nitrophenyl ß-D-glucoside (M)')
#    plt.ylabel('Observed rate (1/min)')
#   
#    plt.subplot(132)
#    plt.scatter(fit['x'], fit['y'])
#    plt.plot(fit['mm_x'], fit['mm_y']) 
#    plt.title("kcat=%2.2f ± %0.2f percent \n km=%2.4f ± %0.2f percent" 
#        % (fit['kcat'], fit['err1']/fit['kcat']*100, fit['km'], fit['err2']/fit['km']*100) )
#    plt.xlabel('4-nitrophenyl ß-D-glucoside (M)')
#
#    plt.subplot(133)
#    plt.scatter(fit['x'], fit['y'])
#    plt.plot(fit['lm_x'], fit['lm_y']) 
#    plt.title("kcat/km=%2.2f ± %2.3f\nr^2=%1.2f" % (fit['eff'], fit['err3'], fit['R']**2) )
#    plt.xlabel('4-nitrophenyl ß-D-glucoside (M)')
#    
#    plt.show()
#

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt 

for thing in ['kcat', 'km', 'eff']:
    y_pos = np.arange(len(fits['sample']))
    plt.barh(y_pos, fits[thing]) 
    plt.gca().set_yscale('log')
    plt.yticks(y_pos, fits['sample'])
    plt.savefig('%s.pdf' % thing)

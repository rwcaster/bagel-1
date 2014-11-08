from pandas import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import linspace
import numpy as np
from sklearn import datasets, linear_model

csv=read_csv('compiled.csv')
csv=csv._get_numeric_data()

def y(m, x, b): return m*x+b

for col1 in csv.columns:
  for col2 in ['kcat', 'km', 'eff']:
    if col1 is not col2:
     
      # regression
      print("Regression on %s versus %s" % (col1, col2))
      param, cov = curve_fit( y, csv[col1], csv[col2], p0=(1,0) )
      resid = y(param[0], csv[col1], param[1]) - csv[col1]
      fres = sum(resid**2)
      error = [ abs(cov[i][i])**0.5 for i in range(len(param)) ]
      print("Params: ", param, "Error:", error)
      xdata = linspace( min(csv[col1]), max(csv[col1]) )
      ydata = [ y(param[0], x, param[1]) for x in xdata ]

      # plot
      print("Making plot %s versus %s" % (col1, col2))
      plt.scatter(csv[col1], csv[col2])
      plt.plot(xdata, ydata)
      plt.xlabel(col1)
      plt.ylabel(col2)
      plt.title("%s versus %s" % (col1,col2) )
      plt.savefig("versus/%s-versus-%s.png" % (col1,col2), format='png')
      plt.clf()

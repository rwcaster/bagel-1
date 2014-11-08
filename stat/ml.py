import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from pandas import read_csv

csv=read_csv('compiled.csv')
csv=csv._get_numeric_data()
csv=csv.as_matrix()

target = 'eff'

X = csv[target]
X_train = X[:-10]
X_test = X[-10:]

y_train = csv[:-10]
y_test  = csv[-10:]

print(X_test, y_test)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

print("Coef: \n", regr.coef_)
print("Residual sum of squares: %.2f" 
  % np.mean((regr.predict(X_test) - y_test) ** 2))

plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, regr.predict(X_test), color="green")
plt.show()

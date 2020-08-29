#pdf application 

import numpy as np;
import pandas as pd;
from matplotlib.pyplot import *;


def MarvellousPredictor():
	#load data
	X = [1,2,3,4,5];
	Y = [3,4,2,4,5];

	print("Mean of Independent variable x :",X);
	print("Mean of Dependent variable y : ",Y);

	#Least Square Method
	mean_x = np.mean(X);
	mean_y = np.mean(Y);

	print("Mean of Independent variable x :",mean_x);
	print("Mean of Dependent variable y : ",mean_y);
	n = len(X);

	numerator = 0;
	denomenator = 0;
	
	#equation of line is y = mx + c
	for i in range(n):
		numerator += (X[i] - mean_x)*(Y[i] - mean_y);

		denomenator += (X[i] - mean_x)**2;

	m = numerator / denomenator;

	#c = Y' - mx'
	c = mean_y - (m * mean_x);

	print("Slope of Regression line is : ",m);				# 0.4
	print("Y intercept of regression line is : ",c);		# 2.4

	
	#Findout goodness of fit i.e R square
	ss_t = 0;
	ss_r = 0;
	
	for i in range(n):
		y_pred = c + m * X[i];
		ss_t = (Y[i] - mean_y)**2;
		ss_r = (Y[i] - y_pred)**2;

	r2 = 1 - (ss_r/ss_t);
	print("Goodness of fit using r2 menthod is ",r2);

def main():
	print(" Linear Regression ");
	MarvellousPredictor();

if __name__ == "__main__":
	main();

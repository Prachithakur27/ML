# Head brain dataset using linear regression 

import numpy as np;
import pandas as pd;
#import matlab.pyplot as plt;

def HeadBrain():
	# Load data
	data = pd.read_csv("MarvellousHeadBrain.csv");
	print(data);

	print("Size if data set",data.shape);

	X = data['Head Size(cm^3)'].values;
	Y = data['Brain Weight(grams)'].values;

	# Least Square Method
	mean_x = np.mean(X);
	mean_y = np.mean(Y);

	n = len(X);
	
	numerator = 0;
	denomenator = 0;
	
	# Equation of line is y = mx + c
	
	for i in range(n):
		numerator += (X[i] - mean_x)*(Y[i]-mean_y);
		denomenator += (X[i] - mean_x)**2;

	m = numerator / denomenator;
	
	c = mean_y - (m * mean_x);
	
	print("Slope of Regression line is ",m);
	print("Y intercept of Regression line is",c);

	max_x = np.max(X) + 100;
	min_x = np.min(X) - 100;

	# Display plotting of above points 
	#x = np.linspace(min_x,max_x,n);
	
	#y = c + m * x

	
	#plt.plot(x,y,color =)

	# Findout goodness of fit i.e R Square
	ss_t = 0;
	ss_r = 0;

	for i in range(n):
		y_pred = c + m*X[i];
		ss_t += (Y[i] - mean_y)**2;
		ss_r += (Y[i] - y_pred)**2;

	r2 = 1 - (ss_r/ss_t);
	print(r2);


def main():
	print("Head brain size predictor using linear regression ");
	HeadBrain();


if __name__ == "__main__":
	main();

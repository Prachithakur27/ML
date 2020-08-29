#Linear regression program by me

def LinearRegression():
	X = [1,2,3,4,5]
	Y = [3,4,2,4,5]

	Xbar = 0;
	Ybar = 0;
	
	for i in range(len(X)):
		Xbar = (X[i] + Xbar);
		Ybar = (Y[i] + Ybar);

	Xmean = Xbar/len(X);
	Ymean = Ybar/len(Y);
 
	print("X mean : ",Xmean);					#3.0
	print("Y mean : ",Ymean);					#3.6

	# m = ((X-Xbar)*(Y-Ybar))/(X-Xbar)**2

	num = 0;
	deno =0 ;

	for i in range (len(X)):
		num += (X[i] - Xmean)*(Y[i] - Ymean);

		deno += (X[i] - Xmean)**2;

	M = num / deno;
	print("Slope of regression line : ",M); 				#0.4

	#C = y - mx
	
	C = (Ymean - M * Xmean);

	print("Y intercept of regression line : ",C);			#2.4 

	# yp = mx+c
	# R square method for goodness of fit 

	N =	0 ;
	D = 0;
	
	for i in range(len(X)):
		yp = M*(X[i]) + C;
		N += (Y[i] - yp)**2 ;
		D += (Y[i] - Ymean)**2 ;

	#print(N);				3.5999999999999996
	#print(D);				5.2 
	r2 = 1 - (N/D);
	print("Goodness of fit using r2 method : ",r2);	

def main():
	print("Linear Regression by me ")
	LinearRegression();

if __name__ == "__main__":
	main();

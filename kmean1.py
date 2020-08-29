'''Application 13
Unsupervised Machine Learning
Clustering using K Mean Algorithm
Consider below Machine Learning application which implements K mean
Algorithm for randomly generated dataset.'''

import numpy as np;
import pandas as pd;
from copy import deepcopy;
from matplotlib import pyplot as plt;

def MarvellousKMean():
	#set three centers,the model should predict similar results

	center_1 = np.array([1,1]);
	print(center_1);

	center_2 = np.array([5,5]);
	print(center_2);
	
	center_3 = np.array([8,1]);
	print(center_3);

	#Generate random data and center it to the three centers

	data_1 = np.random.randn(7,2) + center_1;
	print("Elements of first cluster with size"+str(len(data_1)));
	print(data_1);

	data_2 = np.random.randn(7,2) 
def main():
	print("-------Marvellous Infosystem by piyush khairnar-------");
	print("Unsuervised Machine Learning ");
	print("Clustering using K Mean Algorithm");

	MarvellousKMean();

if __name__ == "__main__":
	main();

# calculate accuracy

from sklearn import tree;
from sklearn.datasets import load_iris;
from sklearn.metrics import accuracy_score;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn.model_selection import train_test_split;

def MarvellousCalculateAccuracyDecisionTree():
	iris = load_iris() #step1 = load data
	
	data = iris.data           #feacture
	target = iris.target       #label

	data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5);           	#split method to split data

	clf = tree.DecisionTreeClassifier()        #algo
	clf.fit(data_train,target_train);
	prediction = clf.predict(data_test);

	Accuracy = accuracy_score(target_test,prediction);
	
	return Accuracy;

def MarvellousCalculateAccuracyKNeighbor():
	iris = load_iris() #step1 = load data
	
	data = iris.data           #feacture
	target = iris.target       #label

	data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5);           	#split method to split data

	clf = KNeighborsClassifier()        #algo
	clf.fit(data_train,target_train);
	prediction = clf.predict(data_test);

	Accuracy = accuracy_score(target_test,prediction);
	
	return Accuracy;

def main():
	Accuracy = MarvellousCalculateAccuracyDecisionTree();
	print("Accuracy of classification algorithm with Decision Tree Classifier is",Accuracy*100,"%");

	Accuracy = MarvellousCalculateAccuracyKNeighbor();
	print("Accuracy of classification algorithm with K Neighbor classifier is",Accuracy*100,"%");

if __name__ == "__main__":
	main();


''' output 
 python3 iris4.py
Accuracy of classification algorithm with Decision Tree Classifier is 94.66666666666667 %
Accuracy of classification algorithm with K Neighbor classifier is  96.0 %
'''

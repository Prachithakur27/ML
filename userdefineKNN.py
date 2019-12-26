from sklearn import tree;
from scipy.spatial import distance;
from sklearn.model_selection import train_test_split;
from sklearn.datasets import load_iris;
from sklearn.metrics import accuracy_score 

def euc(a,b):
	return distance.euclidean(a,b);

class MarvellousKNN():
	def fit(self,TrainingData,TrainingTarget):
		self.TrainingData = TrainingData;
		self.TrainingTarget = TrainingTarget;

	def Predict(self,TestData):
		prediction = [];
	
		for row in TestData:
			label = self.closest(row);
			prediction.append(label);

		return prediction;

	def closest(self,row):
		bestdistance = euc(row,self.TrainingData[0]);
		bestindex = 0;
		
		for i in range(1,len(self.TrainingData)):
			dist = euc(row,self.TrainingData[i]);
			if dist < bestdistance:
				bestdistance = dist;
				bestindex = i;
	
		return self.TrainingTarget[bestindex];

	
def MarvellousKNeighbor():
	border = "-"*50;

	iris = load_iris();

	data = iris.data;
	target = iris.target;
	
	print("Actual data set : ");
	
	for i in range(len(iris.target)):
		print("ID : %s,Feature : %s,Label : %s"%(i,iris.data[i],iris.target[i]));
	
	data_train,data_test,target_train,target_test = train_test_split(data,target,test_size=0.5);

	print(border);

	print("Training data set");
	for i in range(len(data_test)):
		print("ID : %s,Feature : %s,Label : %s"%(i,data_train[i],target_train[i]));
	print("size of training data set %d"%(i+1));


	print("Test data set");
	for i in range(len(data_test)):
		print("ID : %s,Feature : %s,Label : %s"%(i,data_test[i],target_test[i]));
	print("size of training data set %d"%(i+1));

	clf = MarvellousKNN();
	
	clf.fit(data_train,target_train);
	
	prediction = clf.Predict(data_test);
	
	Accuracy = accuracy_score(target_test,prediction);
	
	return Accuracy;
	
def main():
	Accuracy = MarvellousKNeighbor();
	print("Accuracy of classification algorithm with K Neighbor classifier is",Accuracy*100,"%");


if __name__ == "__main__":
	main();

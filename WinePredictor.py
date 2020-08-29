import pandas as pd;
from sklearn import tree;
from sklearn.model_selection import train_test_split;
from sklearn.neighbors import KNeighborsClassifier;

def WinePredictor(data_path):
	data = pd.read_csv(data_path);

	print("Size of actual data : ",len(data));

	feature_names = ["Alcohot","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"];

	print("Names of features : ",feature_names);

	#Alcohot = pd.DataFrame(data_path.Alcohot);
	#print(Alcohot);

	label = ["class"];
	print("Labels : ",label);
	
	feature_names_train,feature_names_test,label_train,label_test = train_test_split(feature_names,label,test_size = 0.3);

	classifier = KNeighborsClassifier();
	classifier.fit(features_names_train,label_train);
	prediction = classifier.predict(features_names_test);
	
def main():
	WinePredictor("WinePredictor.csv")


if __name__ == "__main__":
	main();

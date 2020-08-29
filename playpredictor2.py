import pandas as pd;
from sklearn import tree;
#from sklearn.metrics import accuracy_score;
from sklearn.neighbors import KNeighborsClassifier;
from sklearn import preprocessing;

def PlayPredictor(data_path):
	data = pd.read_csv(data_path,index_col=0);
	
	print("Size of actual dataset",len(data));

	feature_names = ['Wether','Temperature'];

	print("Names of features",feature_names);

	weather = data.Wether;
	Temperature = data.Temperature;
	play = data.Play
	
	le = preprocessing.LabelEncoder();
	weather_encoded = le.fit_transform(weather);
	print(weather_encoded);

	temp_encoded = le.fit_transform(Temperature);
	label = le.fit_transform(play);

	print(temp_encoded);
	
	features = list(zip(weather_encoded,temp_encoded))
	
	model = KNeighborsClassifier(n_neighbors= 3)

	model.fit(features,label);

	predicated = model.predict([[0,2]])
	print(predicated)

def main():
	print("Machine learning application");

	print("Play Predictor application");

	PlayPredictor("MarvellousInfosystems_PlayPredictor.csv")

if __name__ == "__main__":
	main();




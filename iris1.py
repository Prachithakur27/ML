from sklearn.datasets import load_iris;
	
iris = load_iris();

print("Features of iris data set : ");
print(iris.feature_names);

print("target of iris data set : ");
print(iris.target_names);

for i in range(len(iris.target)):
	print("ID:%d,Label:%s,Feature:%s"%(i,iris.data[i],iris.target[i]));

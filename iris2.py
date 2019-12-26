from sklearn.datasets import load_iris;
import numpy as np;
from sklearn import tree;

iris = load_iris();

print("Feature of iris dataset : ");
print(iris.feature_names);

print("target of iris dataset : ");
print(iris.target_names);

#Indix of removed elements
test_index = [1,51,101];

#traning data with remove element
train_target = np.delete(iris.target,test_index);
train_data = np.delete(iris.data,test_index,axis = 0);

#testing data for testing on training data
test_target = iris.target[test_index];
test_data = iris.data[test_index];

clf = tree.DecisionTreeClassifier();

clf.fit(train_data,train_target);

print("values that we removed for testing");
print(test_target);

print("result of testing ");
print(clf.predict(test_data));



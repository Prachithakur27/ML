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


#visualization
#https://scikit-learn.org/stable/modules/tree.html
from sklearn.externals.six import StringIO;
import pydot;

dot_data = StringIO();

dot_data = tree.export_graphviz(clf, out_file=dot_data, 
                      feature_names=iris.feature_names,  
                      class_names=iris.target_names,  
                      filled=True, rounded=True,impurity = False);

graph = pydot.graph_from_dot_data(dot_data.getvalue()); 

graph[0].write_pdf("iris.pdf");

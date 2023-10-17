import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from model import DecisionTree as DecisionTree

data = datasets.load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTree()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = np.sum(y_test == y_pred) / len(y_test)
print(accuracy)
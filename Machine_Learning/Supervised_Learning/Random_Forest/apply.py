from sklearn.model_selection import train_test_split
import numpy as np
from RandomForest import RandomForest
import pandas as pd

df = pd.read_csv("../Decision_Tree/data/data.csv")

y = df['Classification']
X = df.drop(columns = 'Classification')

X_train, X_test, y_train, y_test = train_test_split(X.values, y.values.reshape(-1, 1), test_size=0.2, random_state=42)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

clf = RandomForest(n_trees=20)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc =  accuracy(y_test, predictions)
print(acc)
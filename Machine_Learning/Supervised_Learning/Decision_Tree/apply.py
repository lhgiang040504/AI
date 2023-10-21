import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from model import DecisionTree as DecisionTree

df = pd.read_csv("data/data.csv")

y = df['Classification']
X = df.drop(columns = 'Classification')

X_train, X_test, y_train, y_test = train_test_split(X.values, y.values.reshape(-1, 1), test_size=0.2, random_state=42)

model = DecisionTree(helper_func='CART')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = np.sum(y_test == y_pred)
print(y_pred)

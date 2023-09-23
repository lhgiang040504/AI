import numpy as np

class LogisticRegression:
    def __init__(self, learninng_rate=0.1, num_iters=1000):
        self.learning_rate = learninng_rate
        self.num_iters = num_iters
        self.coefficent = None
        self.classes = None
    
    def _add_bias(self, feature):
        """
        input:
            x: np.arr (obsers, feature)
        output:
             : an np.arr (obsers, feature + 1)
        """
        bias = np.zeros((feature.shape[0], 1))
        feature = np.concatenate((feature, bias), axis=1) # update x that has bias column at the last column
        """
            axis = [0, 1]
                0 append at row
                1 append at columns
            (a, b)
                a will be appended at front of b
        """
        return feature

    def _softmax(self, z):
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    def _one_hot_encoding(self, labels):
        """
        input:
            labels : np.arr (obsers, 1) type: be considered as string
        output:
            : an np.arr (obsers, num_classes)
        """
        num_classes = len(self.classes)
        num_observations = labels.shape[0]
        encoded = np.zeros((num_observations, num_classes))
        for i, label in enumerate(labels):
            encoded[i, label] = 1
        return encoded
    
    def fit(self, observations, labels):
        self.classes = np.unique(labels)
        num_features = observations.shape[1]
        num_classes = len(self.classes)

        self.coefficent = np.zeros((num_classes, num_features + 1)) # (num_classes, num_features + 1)

        observations = self._add_bias(observations) # (obsers, num_features + 1)
        labels = self._one_hot_encoding(labels)
        
        for _ in range(self.num_iters):
            scores = np.dot(observations, self.coefficent.T) # (obsers, num_classes)
            probabilities = self._softmax(scores) # (obsers, num_classes)
            
            error = probabilities - labels
            gradient = np.dot(error.T, observations) # (num_classes, num_features + 1)
            self.coefficent -= gradient * self.learning_rate 
           
    def predict(self, observations):
        observations = self._add_bias(observations)
        scores = np.dot(observations, self.coefficent.T)
        probabilities = self._softmax(scores)
        return np.argmax(probabilities, axis=1)


import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
len(X_train)

# Create an instance of LogisticRegression
lr = LogisticRegression()

# Train the model
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr.predict(X_test)

# Calculate accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

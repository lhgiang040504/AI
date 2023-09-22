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
            x: np.arr (obser, feature)
        output:
             : an np.arr (obser, feature + 1)
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
        return exp_z / np.sum(exp_z)
    
    def _one_hot_encoding(self, labels):
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

        self.coefficent = np.zeros((num_classes, num_features+1))

        observations = self._add_bias(observations)
        labels = self._one_hot_encoding(labels)
        
        for _ in range(self.num_iters):
            scores = np.dot(observations, self.coefficent)
            probabilities = self._softmax(scores)
            
            error = probabilities - labels
            gradient = np.dot(X.T, error)
            self.coefficent -= self.learning_rate * gradient
           
    def predict(self, observations):
        observations = self._add_bias(observations)
        scores = np.dot(observations, self.coefficent)
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
bias = np.zeros((X.shape[0], 1))
print(np.concatenate((bias, X)))
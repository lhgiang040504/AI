import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.001):
        self.learning_rate = learning_rate
        self.bias = None
        self.weight = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def _initialize_parameters(self, num_features):
        self.weight = np.zeros(num_features) # (num_features, )
        self.bias = 0

    def _compute_gradient(self, x_train, y_train):
        num_samples = x_train.shape[0]
        num_features = x_train.shape[1]

        prediction = self._sigmoid(x_train * self.weight + self.bias) # (num_examples, num_features) * (num_features, 1)

        dư = (1 / num_samples) * np.dot(x_train.T, prediction - y_train)
        db = (1 / num_samples) * np.sum(prediction - y_train)

    def _update_parameters(self, dw, db):
        self.weight -= self.learning_rate * dw
        self.bias -= self.learning_rate * db


import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.001, num_iters=1000):
        self.learning_rate = learning_rate
        self.num_iters = num_iters
        self.bias = None
        self.weight = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def _initialize_parameters(self, num_features):
        self.weight = np.zeros(num_features) # (num_features, )
        self.bias = 0

    def _compute_gradient(self, x_train, y_train):
        num_samples = x_train.shape[0]

        prediction = self._sigmoid(np.dot(x_train, self.weight) + self.bias) # (num_examples, num_features) * (num_features, 1)

        dw = (1 / num_samples) * np.dot(x_train.T, prediction - y_train)
        db = (1 / num_samples) * np.sum(prediction - y_train)

        return dw, db

    def _update_parameters(self, dw, db):
        self.weight -= self.learning_rate * dw
        self.bias -= self.learning_rate * db

    def fit(self, x_train, y_train):
        num_features = x_train.shape[1]

        self._initialize_parameters(num_features)

        for iiter in range(self.num_iters):
            dw, db = self._compute_gradient(x_train, y_train)
            self._update_parameters(dw, db)

    def predict(self, x_test):
        return self._sigmoid(np.dot(x_test, self.weight)  + self.bias)


    @property
    def coef(self):
        return self.weight[1:]
    
    @property
    def intercept(self):
        return self.bias
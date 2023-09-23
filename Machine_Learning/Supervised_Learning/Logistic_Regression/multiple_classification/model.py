import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.1, num_iters=1000):
        self.learning_rate = learning_rate
        self.num_iters = num_iters
        self.coefficient = None
        self.classes = None
    
    def _add_bias(self, features):
        """
        Add a bias column to the features matrix.
        
        Args:
            features: np.array of shape (observations, features)
        
        Returns:
            np.array of shape (observations, features + 1): features matrix with a bias column added
        """
        bias = np.ones((features.shape[0], 1))
        features_with_bias = np.concatenate((features, bias), axis=1)
        return features_with_bias

    def _softmax(self, z):
        """
        Compute the softmax function for the given array of scores.
        
        Args:
            z: np.array of shape (observations, num_classes)
        
        Returns:
            np.array of shape (observations, num_classes): softmax probabilities
        """
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    def _one_hot_encoding(self, labels):
        """
        Perform one-hot encoding for the given array of labels.
        
        Args:
            labels: np.array of shape (observations, 1) with string labels
        
        Returns:
            np.array of shape (observations, num_classes): one-hot encoded labels
        """
        num_classes = len(self.classes)
        encoded = np.zeros((labels.shape[0], num_classes))
        for i, label in enumerate(labels):
            encoded[i, label] = 1
        return encoded
    
    def fit(self, observations, labels):
        """
        Fit the logistic regression model to the training data.
        
        Args:
            observations: np.array of shape (observations, features) representing the training data
            labels: np.array of shape (observations, 1) representing the training labels
        """
        self.classes = np.unique(labels)
        num_features = observations.shape[1]
        num_classes = len(self.classes)

        self.coefficient = np.zeros((num_classes, num_features + 1))  # (num_classes, num_features + 1)

        observations_with_bias = self._add_bias(observations)  # (observations, num_features + 1)
        labels_encoded = self._one_hot_encoding(labels)
        
        for _ in range(self.num_iters):
            scores = np.dot(observations_with_bias, self.coefficient.T)  # (observations, num_classes)
            probabilities = self._softmax(scores)  # (observations, num_classes)
            
            error = probabilities - labels_encoded
            gradient = np.dot(error.T, observations_with_bias)  # (num_classes, num_features + 1)
            self.coefficient -= self.learning_rate * gradient
           
    def predict(self, observations):
        """
        Predict the class labels for the given observations.
        
        Args:
            observations: np.array of shape (observations, features) representing the test data
        
        Returns:
            np.array of shape (observations,): predicted class labels
        """
        observations_with_bias = self._add_bias(observations)
        scores = np.dot(observations_with_bias, self.coefficient.T)
        probabilities = self._softmax(scores)
        return np.argmax(probabilities, axis=1)
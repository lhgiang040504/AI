import numpy as np

class LogisticRegression:
    def __init__(self, learninng_rate=0.1, num_iters=1000):
        self.learning_rate  = learninng_rate
        self.num_iters      = num_iters
        self.coefficent     = None
        self.classes        = None
    
    def _add_bias(self, features):
        """
        Add bias column to the features matrix.
        
        Args:
            features: np.array of shape (observers, features)
        
        Returns:
            np.array of shape (observers, features + 1): features matrix with bias column added
        """
        bias = np.ones((features.shape[0], 1))
        features = np.concatenate((features, bias), axis=1) # update x that has bias column at the last column
        return features

    def _softmax(self, z):
        """
        Compute the softmax function for the given array of scores.
        
        Args:
            z: np.array of shape (observers, num_classes)
        
        Returns:
            np.array of shape (observers, num_classes): softmax probabilities
        """
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    def _one_hot_encoding(self, labels):
        """
        Perform one-hot encoding for the given array of labels.
        
        Args:
            labels: np.array of shape (observers, 1) with string labels
        
        Returns:
            np.array of shape (observers, num_classes): one-hot encoded labels
        """
        num_classes = len(self.classes)
        num_observations = labels.shape[0]
        encoded = np.zeros((num_observations, num_classes))
        for i, label in enumerate(labels):
            encoded[i, label] = 1
        return encoded
    
    def fit(self, observations, labels):
        """
        Fit the logistic regression model to the training data.
        
        Args:
            observations: np.array of shape (observers, features) representing the training data
            labels: np.array of shape (observers, 1) representing the training labels
        """
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
            self.coefficent -= self.learning_rate * gradient
           
    def predict(self, observations):
        """
        Predict the class labels for the given observations.
        
        Args:
            observations: np.array of shape (observers, features) representing the test data
        
        Returns:
            np.array of shape (observers,): predicted class labels
        """
        observations = self._add_bias(observations)
        scores = np.dot(observations, self.coefficent.T)
        probabilities = self._softmax(scores)
        return np.argmax(probabilities, axis=1)
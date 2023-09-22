import numpy as np

class LosgisticRegression:
    def __init__(self, learninng_rate=0.01, num_iters=1000):
        self.learning_rate = learninng_rate
        self.num_iters = num_iters
        self.coefficent = None
    
    def _softmax(self, z):
        exp_z = np.exp(z)
        return exp_z / np.sum(exp_z)
    
    def _one_hot_encoding(self, labels):
        num_classes = labels.nunique()
        num_observations = labels.shape[0]
        encoded = np.zeros((num_observations, num_classes))
        
        for i, label in enumerate(labels):
            encoded[i, label] = 1
        return encoded
    
    
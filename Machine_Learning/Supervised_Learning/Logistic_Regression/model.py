import numpy as np

class LogisticRegression:
    def __init__(self):
        self.weight = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def _initialize_parameters(self, num_feature):
        self.weight = np.ones((num_feature))
        # np.ones(num_feature)
import numpy as np

class LinearRegression:
    def __init__(self):
        """
        This is a numpy array that :
        each column is correspond to each feature
        each row is corresponf to each observation
        """
        self.weights = None

    def compute(self, features, labels):
        try:
            self.weights = np.dot(np.dot(np.linalg.inv(np.dot(features.T, features)), features.T), labels)
        except:
            raise Exception

    def fit(self, features, labels):
        # Handle input parameters
            # For features
        features = np.array(features)
        add_ForIntercept = np.ones(features.shape[0]) # 0 is num of rows, 1 is num of columns // (rows, columns)
        features = np.c_[add_ForIntercept, features] # concatenate
            # For lable
        labels = np.array(labels)

        self.compute(features, labels)
    
    """
    The @property decorator in Python is used to define "getter" methods for class attributes. 
    It allows you to access an attribute like a method, but without using parentheses.
    """
    @property
    def coef(self):
        return self.weights[1:]
    
    @property
    def intercept(self):
        return self.weights[0]
    
    def predict(self, features):
        try:
            features = np.array(features)
            add_ForIntercept = np.ones(features.shape[0]) 
            features = np.c_[add_ForIntercept, features]

            result = np.dot(features, self.weights)
            return result
        except:
            raise Exception
      
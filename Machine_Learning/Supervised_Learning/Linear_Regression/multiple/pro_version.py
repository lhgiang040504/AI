import numpy as np
class Multiple_LinearRegression:
    def __init__(self, learning_rate = 0.0000001, n_iter = 1000):
        """
        This is a numpy array that :
        each column is correspond to each feature
        each row is corresponf to each observation
        """
        self.weights = None
        self.bias = None
        self.learning_rate = learning_rate
        self.n_iter = n_iter

    def compute(self, features, labels):
        """
        features (obs, fea)
        labels (obs, 1)
        """
        n_observation, n_feature = features.shape # [obs, fea]
        self.weights = np.ones(n_feature).reshape(-1, 1) # (fea, 1)
        self.bias = 0
                
        for iter in range(self.n_iter):
            # Calculate the predicted values
            labels_pred = np.dot(features, self.weights) + self.bias # (obs, 1)
            labels = labels.reshape(n_observation, 1)
                        
            # Compute the gradients
            dw = np.dot(features.T, (labels_pred - labels)) / n_observation # (fea, 1)
            db = np.sum(labels_pred - labels) / n_observation 
            
            # Update weights and bias
            self.weights -= dw * self.learning_rate # Error cause wrong shape, expect (fea, 1) but return (fea, obs)
            self.bias -= db * self.learning_rate

    def fit(self, features, labels):
        # Handle input parameters
        # For features
        features = features.values
        # For lable
        labels = labels.values
         
        self.compute(features, labels)
    
    """
    The @property decorator in Python is used to define "getter" methods for class attributes. 
    It allows you to access an attribute like a method, but without using parentheses.
    """
    @property
    def coef(self):
        return self.weights
    
    @property
    def intercept(self):
        return self.bias
    
    def predict(self, features):
        features = features.values
        return np.dot(features, self.weights) + self.bias
    
    def R_Squared(label_true, label_pred):
        """
        Compute R-squared (coefficient of determination) for a linear regression model.
        
        Parameters:
        - label_true: Array-like, true values of the dependent variable.
        - label_pred: Array-like, predicted values of the dependent variable from the model.

        Returns:
        - R-squared value, a float between 0 and 1.
        """
        # Calculate the mean of the true values
        mean_label_true = np.mean(label_true)
        # Calculate the total sum of squares 
        ss_fit = np.sum((label_pred - mean_label_true)**2)
        # Calculate the residual sum of squares
        ss_mean = np.sum((label_true - mean_label_true)**2)
        # Calculate R-squared
        r_squared = 1 - (ss_fit/ss_mean)

        return r_squared
    
    def MSE(self, label_true, label_pred):
        """
        Compute the Mean Squared Error (MSE) for a linear regression model.

        Parameters:
        - label_true: Array-like, true values of the dependent variable.
        - label_pred: Array-like, predicted values of the dependent variable from the model.

        Returns:
        - Mean Squared Error (MSE), a non-negative float.
        """
        label_true = label_true.values
        mse = np.mean((label_pred - label_true)**2)

        return mse
    
    def RMSE(self, label_true, label_pred):
        """
        Compute the Root Mean Squared Error (RMSE) for a linear regression model.

        Parameters:
        - label_true: Array-like, true values of the dependent variable.
        - label_pred: Array-like, predicted values of the dependent variable from the model.

        Returns:
        - Root Mean Squared Error (RMSE), a non-negative float.
        """
        rmse = np.sqrt(self.MSE(label_true, label_pred))

        return rmse

    def MAE(self, label_true, label_pred):
        """
        Compute the Mean Absolute Error (MAE) for a linear regression model.

        Parameters:
        - label_true: Array-like, true values of the dependent variable.
        - label_pred: Array-like, predicted values of the dependent variable from the model.

        Returns:
        - Mean Absolute Error (MAE), a non-negative float.
        """
        mae = np.mean(np.abs(label_pred - label_true))

        return mae
    

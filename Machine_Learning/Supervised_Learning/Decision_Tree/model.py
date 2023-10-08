import numpy as np

class Decision_Tree:
    def __init__(self, max_depth=None):
        self.tree = {}

    def gini(self, y):
        """
        parameters: 
            y : Label of observations based on specified features within threshold.
        return:
            gini_impurity : Impurity values of y.
        """
        # Calculate the Gini Impurity of a target variable
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini_impurity = 1 - np.sum(probabilities ** 2)
        
        return gini_impurity
    
    def gini_index(self, X, y, feature_idx, threshold):
        """
        parameters:
            X : The feature matrix, where each row represents a sample and each column represents a feature.
            y : The target variable, which contains the corresponding class labels for each sample.
            feature_idx : The index of the feature for which the Gini index is calculated.
            threshold :  The threshold value used to split the data based on the specified feature.
        return:

        """
        # Split the data based on the given threshold and feature
        left_mask = X.iloc[:, feature_idx] <= threshold
        right_mask = X.iloc[:, feature_idx] > threshold
        y_left = y[left_mask]
        y_right = y[right_mask]

        # Calculate the Gini Impurity of the left and right subsets
        gini_left = self.gini(y_left)
        gini_right = self.gini(y_right)

        # Calculate the Gini Index
        len_left = len(y_left)
        len_right = len(y_right)
        len_total = len(y)
        gini_index = (len_left / len_total) * gini_left + (len_right / len_total) * gini_right
        
        return gini_index
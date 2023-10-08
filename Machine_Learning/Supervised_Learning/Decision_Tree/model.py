import numpy as np

class Decision_Tree:
    def __init__(self, max_depth=None):
        self.tree = {}

    def gini(self, y):
        """
        parameters: 
            y : label of observations base on certain features within threshold
        return:
            gini_impurity : impurity values of y
        """
        # Calculate the Gini Impurity of a target variable
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini_impurity = 1 - np.sum(probabilities ** 2)
        return gini_impurity
    
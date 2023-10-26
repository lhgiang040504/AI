from DecisionTree import DecisionTree
import numpy as np

class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, min_samples_split=5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

    def fit(self, X, y):
        pass

    def _boosttrap_samples(self, X, y):
        pass

    def _most_common_label(self):
        pass

    def predict(self):
        pass
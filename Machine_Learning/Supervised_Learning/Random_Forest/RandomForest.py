from DecisionTree import DecisionTree
import numpy as np

class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, min_samples_split=5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.forest = None

    def fit(self, X, y):
        self.forest = []
        for _ in range(self.n_trees):
            # Call the Decisiontree model
            tree = DecisionTree(max_depth=self.max_depth, 
                                min_sample=self.min_samples_split, 
                                helper_func="ID3")
            # Bootstrap data
            X_bootstrap, y_bootstrap = self._boosttrap_data(X, y)
            
            # Build tree, a part of n_trees
            tree.fit(X_bootstrap, y_bootstrap)

            # Add new tree to forest
            self.forest.append(tree)



    def _boosttrap_samples(self, X, y):
        n_samples = X.shape[0]
        indices = np.random.randint(0, n_samples, size=(n_samples))
        return X[indices], y[indices]

    def _most_common_label(self):
        pass

    def predict(self):
        pass
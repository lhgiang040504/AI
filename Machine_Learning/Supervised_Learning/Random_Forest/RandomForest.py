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
            X_bootstrap, y_bootstrap = self._boosttrap_samples(X, y)
            
            # Build tree, a part of n_trees
            tree.fit(X_bootstrap, y_bootstrap)

            # Add new tree to forest
            self.forest.append(tree)



    def _boosttrap_samples(self, X, y):
        n_samples = X.shape[0]
        # indices = np.random.randint(0, n_samples, size=(n_samples)) not satify the require // lower bound and upper bound
        indices = np.random.choice(n_samples, n_samples, replace=True)
        ''' 
        s1 : the range we want to choose in it
        s2 : the size of our choice
        s3 : True if our choice allow duplicates'''
        return X[indices], y[indices]

    def _most_common_label(self, predictions):
        '''
        predictions : list of lists where each rows is a prediction of corresponding obser from forest
        '''
        # Create a set that contain two elements of each rows.
        # First element is the list label predicted of obser and the second is list frequency of each label in first one.
        label_frequency_set = [np.unique(prediction, return_counts=True) for prediction in predictions]
        
        # Get the label that appear with the most time of each predictions obser
        majority_label = [label_frequency[0][np.argmax(label_frequency[1])] for label_frequency in label_frequency_set]
        
        return majority_label    

    def predict(self, X):
        result = []
        for x in X:
            predictions = [tree.predict([x]) for tree in self.forest]
            result.append(predictions)
        
        most_common_labels = self._most_common_label(predictions)  
        return most_common_labels
        
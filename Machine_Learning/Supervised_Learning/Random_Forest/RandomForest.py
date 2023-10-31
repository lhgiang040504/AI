from DecisionTree import DecisionTree
import numpy as np

class RandomForest:
    def __init__(self, n_trees=10, max_depth=10, min_samples_split=5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.forest = []

    def fit(self, X, y):
        for _ in range(self.n_trees):
            # Call the Decisiontree model
            tree = DecisionTree(helper_func="ID3")
            
            # Bootstrap data
            X_bootstrap, y_bootstrap = self._bootstrap_samples(X, y)
            
            # Build tree, a part of n_trees
            tree.fit(X_bootstrap, y_bootstrap)

            # Add new tree to forest
            self.forest.append(tree)

    def _bootstrap_samples(self, X, y):
        """
        parameter : X, y numpy array that are data and target
        
        return : update input to get bootstrap dataset that has Duplicates allowed
        """
        n_samples = X.shape[0]
        # indices = np.random.randint(0, n_samples, size=(n_samples)) not satify the require // lower bound and upper bound
        indices = np.random.choice(n_samples, n_samples, replace=True)
        ''' 
        s1 : the range we want to choose in it
        s2 : the size of our choice
        s3 : True if our choice allow duplicates
        '''
        return X[indices], y[indices]

    
    def _most_common_labels(self, predictions):
        # Create a set that contain of list label and their frequency
        label_frequency_set = np.unique(predictions, return_counts=True)
        
        # Get the label that appear with the most time of each predictions obser
        majority_label = label_frequency_set[0][np.argmax(label_frequency_set[1])] 
        
        return majority_label   
    


    def predict(self, X):
        # Initial a list that contain all prediction of all tree
        # Shape (n_trees, n_sample)
        predictions = []
        for tree in self.forest:
            # Predict X with current tree
            prediction = np.ravel(tree.predict(X).reshape(1, -1))
            # Append to outer list
            predictions.append(prediction)
        
        

        return predictions



        


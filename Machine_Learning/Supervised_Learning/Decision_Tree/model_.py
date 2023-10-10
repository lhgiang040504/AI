import numpy as np

class DecisionTree:
    def __init__(self):
        self.tree = {}

    def entropy(self, y):
        # Calculate the entropy of a target variable
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy

    def information_gain(self, X, y, feature_idx, threshold):
        # Calculate the information gain for a given feature and threshold
        entropy_parent = self.entropy(y)

        # Split the data based on the given feature and threshold
        left_mask = X[:, feature_idx] <= threshold
        right_mask = X[:, feature_idx] > threshold
        y_left = y[left_mask]
        y_right = y[right_mask]

        # Calculate the entropy of the left and right subsets
        entropy_left = self.entropy(y_left)
        entropy_right = self.entropy(y_right)

        # Calculate the information gain
        n_left = len(y_left)
        n_right = len(y_right)
        n_total = len(y)
        information_gain = entropy_parent - (n_left / n_total * entropy_left) - (n_right / n_total * entropy_right)
        return information_gain

    def find_best_split(self, X, y):
        best_gain = 0
        best_feature = None
        best_threshold = None

        for feature_idx in range(X.shape[1]):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                gain = self.information_gain(X, y, feature_idx, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def build_tree(self, X, y):
        # Base case: If all samples belong to the same class, return a leaf node
        if len(np.unique(y)) == 1:
            return {'class': y[0]}

        # Base case: If we have no more features to split on, return the majority class
        if X.shape[1] == 0:
            unique_classes, counts = np.unique(y, return_counts=True)
            majority_class = unique_classes[np.argmax(counts)]
            return {'class': majority_class}

        # Find the best feature and threshold to split the data
        best_feature, best_threshold = self.find_best_split(X, y)

        # Split the data based on the best feature and threshold
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > best_threshold
        X_left, y_left = X[left_mask], y[left_mask]
        X_right, y_right = X[right_mask], y[right_mask]

        # Recursive call to build subtrees
        left_subtree = self.build_tree(X_left, y_left)
        right_subtree = self.build_tree(X_right, y_right)

        # Create the current node with the best feature and threshold
        node = {
            'feature': best_feature,
            'threshold': best_threshold,
            'left': left_subtree,
            'right': right_subtree
        }

        return node

    def predict(self, X):
        return np.array([self.traverse_tree(x, self.tree) for x in X])

    def traverse_tree(self, x, node):
        if 'class' in node:
            return node['class']
        
        if x[node['feature']] <= node['threshold']:
            return self.traverse_tree(x, node['left'])
        else:
            return self.traverse_tree(x, node['right'])
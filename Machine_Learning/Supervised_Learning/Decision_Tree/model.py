import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left_subtree=None, right_subtree=None, *,value):
        self.feature = feature
        self.threshold = threshold
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth=10, min_sample=2):
        self.max_depth = max_depth
        self.min_sample = min_sample
        self.root = None

    def fit(self, X, y):
        self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))
        
        # Base case: If all samples belong to the same class, return a leaf node
        if len(n_labels == 1):
            return Node(value=np.unique(y))

        # Base case : If n_sample reaches the min_sample or max_depth is exceeded, do the majority vote
        if (n_samples <= self.min_sample) or (depth == self.max_depth):
            label_frequency = np.unique(y, return_counts=True)
            majority_label = label_frequency[0][np.argmax(label_frequency[1])]
            return Node(value=majority_label)

        # Find the best feature and threshold to split the data
        best_feature, best_threshold = self._find_Best_Split(X, y)

        # Split the data based on the best feature and best threshold
        X_left, y_lelf, X_right, y_right = self._split(X, y, best_feature, best_threshold)

        # Recursive call to build tree
        left_subtree = self._build_tree(X_left, y_lelf, depth + 1)
        right_subtree = self._build_tree(X_right, y_right, depth + 1)

        # Create the current node with the best feature and best threshold
        node = Node(best_feature, best_threshold, left_subtree, right_subtree)
       
        return node

    def _find_Best_Split(self):
        pass

    def _split(self, X, y, best_feature, best_threshold):
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > best_threshold
        X_left, y_left = X[left_mask], y[left_mask]
        X_right, y_right = X[right_mask], y[right_mask]

        return X_left, y_left, X_right, y_right
         
    def predict(self, X):
        # Predict the class for each instance in X
        return np.array([self._traverse_tree(x, self.root) for x in X])
    
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.lelf_subtree)
        else:
            return self._traverse_tree(x, node.right_subtree)
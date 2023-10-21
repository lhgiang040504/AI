import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left_subtree=None, right_subtree=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth=10, min_sample=2, *, helper_func=None):
        self.max_depth = max_depth
        self.min_sample = min_sample
        self.root = None
        self.type = 1 if helper_func == "CART" else 0

    def fit(self, X, y):
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))
        
        # Base case: If all samples belong to the same class, return a leaf node
        if n_labels == 1:
            return Node(value=np.unique(y))

        # Base case : If n_sample reaches the min_sample or max_depth is exceeded, do the majority vote
        if (n_samples <= self.min_sample) or (depth == self.max_depth):
            label_frequency = np.unique(y, return_counts=True)
            
            if len(label_frequency[0]) == 0:
                return Node()
            else:
                majority_label = label_frequency[0][np.argmax(label_frequency[1])]
                return Node(value=majority_label)

        # Find the best feature and threshold to split the data
        best_feature, best_threshold = self._find_best_split(X, y)

        # Split the data based on the best feature and best threshold
        left_mask, right_mask = self._split(X, y, best_feature, best_threshold)
        X_left, y_lelf = X[left_mask], y[left_mask]
        X_right, y_right = X[right_mask], y[right_mask]

        # Recursive call to build tree
        left_subtree = self._build_tree(X_left, y_lelf, depth + 1)
        right_subtree = self._build_tree(X_right, y_right, depth + 1)

        # Create the current node with the best feature and best threshold
        node = Node(best_feature, best_threshold, left_subtree, right_subtree)
       
        return node

    def _split(self, X, y, best_feature, best_threshold):
        left_mask = X[:, best_feature] <= best_threshold
        right_mask = X[:, best_feature] > best_threshold

        return left_mask, right_mask
    
    def _find_best_split(self, X, y):
        return self._CART_find_best_split(X, y) if self.type == 1 else self._ID3_find_best_split(X, y)
    
    # ---- ID3 algorithm to find best property for splitting
    def _entropy(self, y):
        # Calculate the entropy of a target variable
        _, frequency = np.unique(y, return_counts=True)
        probabilities = frequency / len(y)
        result = -np.sum([probability * np.log(probability) for probability in probabilities if np.greater(probability, 0)])
        return result
    
    def _information_gain(self, X, y, feature_idx, threshold):
        # Calculate entropy of parent node
        parent_entropy = self._entropy(y)

        # Separate data into two groups by the given feature and threshold
        left_mask, right_mask = self._split(X, y, feature_idx, threshold)
        y_left = y[left_mask]
        y_right = y[right_mask]
        if len(y_left) * len(y_right) == 0:
            return 0

        # Calculate the entropy of the left and right subsets
        entropy_left = self._entropy(y_left)
        entropy_right = self._entropy(y_right)

        # Calculate the information gain
        n_left = len(y_left)
        n_right = len(y_right)
        n_total = len(y)
        information_gain = parent_entropy - (n_left / n_total * entropy_left) - (n_right / n_total * entropy_right)
        
        return information_gain
    
    def _ID3_find_best_split(self, X, y):
        best_InforGain = -np.inf
        best_feature = None
        best_threshold = None

        for feature_idx in range(X.shape[1]):
            thresholds = np.unique(X[:, feature_idx])
            
            for threshold in thresholds:
                infor_gain = self._information_gain(X, y, feature_idx, threshold)

                if infor_gain > best_InforGain:
                    best_InforGain = infor_gain
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold
    # ----

    # ---- CART Classification And Regression Tree
    def _gini(self, y):
        """
        parameters: 
            y : Label of observations based on specified features within threshold.
        return:
            gini_impurity : Impurity values of y.
        """
        # Calculate the Gini Impurity of a target variable
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini_impurity = 1 - np.sum(probabilities ** 2)
        
        return gini_impurity
    
    def _gini_index(self, X, y, feature_idx, threshold):
        """
        parameters:
            X : The feature matrix, where each row represents a sample and each column represents a feature.
            y : The target variable, which contains the corresponding class labels for each sample.
            feature_idx : The index of the feature for which the Gini index is calculated.
            threshold :  The threshold value used to split the data based on the specified feature.
        return:
            gini_index : The gini INdex of the split

        """
        # Split the data based on the given threshold and feature
        left_mask, right_mask = self._split(X, y, feature_idx, threshold)
        y_left = y[left_mask]
        y_right = y[right_mask]
        if len(y_left) * len(y_right) == 0:
            return 0

        # Calculate the Gini Impurity of the left and right subsets
        gini_left = self._gini(y_left)
        gini_right = self._gini(y_right)

        # Calculate the Gini Index
        len_left = len(y_left)
        len_right = len(y_right)
        len_total = len(y)
        gini_index = (len_left / len_total) * gini_left + (len_right / len_total) * gini_right
        
        return gini_index
    
    def _CART_find_best_split(self, X, y):
        best_gini_index = np.inf
        best_feature = None
        best_threshold = 0

        for feature_idx in range(X.shape[1]):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                gini_index = self._gini_index(X, y, feature_idx, threshold)
                
                if gini_index < best_gini_index:
                    best_gini_index = gini_index
                    best_feature = feature_idx
                    best_threshold = threshold

        return best_feature, best_threshold
    # ----

    def predict(self, X):
        # Predict the class for each instance in X
        return np.array([self._traverse_tree(x, self.root) for x in X], dtype=object)
    
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left_subtree)
        else:
            return self._traverse_tree(x, node.right_subtree)
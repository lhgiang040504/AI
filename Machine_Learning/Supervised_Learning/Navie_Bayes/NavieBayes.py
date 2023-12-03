import numpy as np

class NavieBayes:
    def __init__(self):
        self._labels = None
        self._samples = None
        self._features = None


    def fit(self, X, y):
        # Get some technical parameters
        self._Num_samples, self._Num_features = X.shape
        self._labels = np.unique(y)
        features = np.arange(self._Num_features)
        
        # Compute Label Conditional Probability
        label_probability = {}
        for label in self._labels:
            label_idx = np.where(y = label)[0]
            label_observation = X[label_idx]
            # Calculate feature probability with conditional label
            feature_probabilities = np.mean(label_observation, axis=0) / self._Num_features
            label_probability[label] = feature_probabilities

        # Visualize information of our dataset
        for label, feature_probabilities in label_probability.items():
            print("Label: ", label)
            for feature, probability in zip(features, feature_probabilities):
                print("Feature: ", feature, "Probability: ", probability)

            print()
        

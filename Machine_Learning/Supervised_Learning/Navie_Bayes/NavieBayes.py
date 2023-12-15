"""
Naive Bayes Classifier Implementation from scratch

To run the code structure the code in the following way:
    X be size: (num_training_examples, num_features)
    y be size: (num_classes, )

Where the classes are 0, 1, 2, etc. Then an example run looks like:
    NB = NaiveBayes(X, y)
    NB.fit(X)
    predictions = NB.predict(X)

Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
*    2020-04-21 Initial coding

"""
import numpy as np

class NavieBayes:
    def __init__(self):
        print("Accept")

    def fit(self, X, y):
        self._labels = np.unique(y)
        self._samples, self._features = X.shape
        self.eps = 1e-6
        
        self.labels_mean = {}
        self.labels_variance = {}
        self.labels_prior = {}

        for label in self._labels:
            ident_label = X[y == label]

            # Calculate mean, variance and probability of each label in trainset
            self.labels_mean[int(label)] = np.mean(ident_label, axis=0)
            self.labels_variance[int(label)] = np.var(ident_label, axis=0)
            self.labels_prior[int(label)] = ident_label.shape[0] / self._samples
            
        print(self.labels_mean)
        print(self.labels_variance)
        print(self.labels_prior)

    def predict(self, X):
        probs = np.zeros((self._samples, len(self._labels)))

        for idx, label in enumerate(self._labels):
            # Captute all necessaty informations of each label
            mean = self.labels_mean[int(label)] # (1, num_features)
            variance = self.labels_variance[int(label)] # (1, num_feature)
            prior = self.labels_prior[int(label)] # (1, 1)

            # Calculate posterior for each class
            probs_label = self.Gaussian_Formular(X, mean, variance)
            probs[:, idx] = probs_label + np.log(prior)
                    
        return np.argmax(probs, axis=1)
    
    def Gaussian_Formular(self, X, mean, variance):
        # Calculate probability from Gaussian density function
        numerator = np.exp(-((X - mean) ** 2 / (2 * variance)))
        denominator = np.sqrt(2 * np.pi * variance)
        posterior = np.sum(np.log(numerator / denominator), axis=1)
        
        return posterior

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
        self._labels = len(np.unique(y))
        self._samples, self._features = X.shape
        # A small value eps used for numerical stability
        self.eps = 1e-6
        
        self.labels_mean = {}
        self.labels_variance = {}
        self.labels_prior = {}

        for label in range(self._labels):
            ident_label = X[y == label]

            # Calculate mean, variance and probability of each label in trainset
            self.labels_mean[str(label)] = np.mean(ident_label, axis=0)
            self.labels_variance[str(label)] = np.mean(ident_label, axis=0)
            self.labels_prior[str(label)] = ident_label.shape[0] / self._samples

    def predeict(self, X):
        probs = np.zeros((self._samples, self._labels))

        for label in range(self._labels):
            # Captute all necessaty informations of each label
            mean = self.labels_mean[str(label)]
            variance = self.labels_variance[str(label)]
            prior = self.labels_prior[str(label)]

            # Calculate posterior for each class
            probs_label = self.Gaussian_Formular(X, mean, variance)
            probs[:, label] = probs_label + np.log(prior)

        return np.argmax(probs_label, 1)
    
    def Gaussian_Formular(self, X, mean, variance):
        # Calculate probability from Gaussian density function
        const = -self._features / 2* np.log(2 * np.pi) - 0.5 * np.sum(np.log(variance + self.eps))
        
        probs = 0.5 * np.sum(np.power(X - mean, 2) / (variance + self.eps), 1)
        return const - probs


if __name__ == "__main__":
    X = np.loadtxt("data/data.txt", delimiter=",")
    y = np.loadtxt("data/targets.txt") - 1

    NB = NavieBayes()
    NB.fit(X, y)
    y_pred = NB.predeict(X)

    print(f"Accuracy: {sum(y_pred==y)/X.shape[0]}")
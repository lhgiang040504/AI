# Decision Tree build model from scratch

1. Description

- Branch : A path of the decision tree starts at an *decision node (internal node)* and ends at the *leaf node (terminal node)*

    - Root node : The highest node of the tree which present the complete dataset, the first start node of the tree.
    
    - Decision node (internal node) : A node that symbolizes a choice regarding an input feature.

    - Leaf node (terminal node) : The end node of each *branch*, the node that contain the label of each observation. Noted that label can be categorical or numerical depend on **model's helper function**.

- Parent node : The node that devide into one or more *child node* depend on **model's helper function**.
- Child nodes: Nodes created by deciosn of the *parent node*.

2. Base run

- Split feature, split point : We need to choose the best ingredient for splitting to get the hight accuracy and so that based on **model's helper function**.

- When to stop splitting : number of samples remaining (min), the depth of tree (height of tree) (max), got leaf not that have pure label or we will  need to do majority vote, imputity decrease(min).

3. Train model

- **model's helper function**

    - Calculate the information gain (ID3, C45) or the gini_index (CART).

    - Split train_dataset with the best feature and the best threshold obtained from the helper's function above.

    - Devide tree and do the same for all created branches until a stopping criteria is reached.

4. Predict
- Which each obsers of test_dataset, following the tree until reach a leaf node.
- Return the prediction value of this leaf node (the most common class label)

5. Explain **model's helper function**

- CART : Classification And Regression Tree

    - Gini_impurity : ```python gini_impurity = 1 - np.sum(probabilities ** 2)```

        - Gini impurity measures the probability of incorrectly classifying a randomly chosen element from a set.

    - Gini_idx : ```python gini_index = (len_left / len_total) * gini_left + (len_right / len_total) * gini_right```

        - The Gini index is a variant of Gini impurity and is used to evaluate the quality of a split in a decision tree.

- ID3 : Is primarily used for classification tasks and handles categorical attributes.

    - Entropy : ```python entropy = -np.sum(probabilities * np.log2(probabilities) ```
        - probability ~ numpy array :  calculated by frequency of each label in labelset divide by labelset.

        - Entropy is the measure of the degree of randomness or uncertainty in the dataset. In the case of classifications, it measures the randomness based on the distribution of class labels in the dataset.

    - Information gain : ```python information_gain = entropy_parent - (n_left / n_total * entropy_left) - (n_right / n_total * entropy_right) ```

        - Information gain measures the reduction in entropy or variance that the results from splitting a dataset based on a specific property. The higher the information gain, the more valuable the feature is in predicting the target variable. 
        


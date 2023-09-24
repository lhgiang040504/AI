The assumptions for Multiple Logistic Regression include:

1.Linearity
2.No Outliers
3.Independence
4.No Multicollinearity

Let’s dive in to each one of these separately.


1.Linearity
Logistic regression fits a logistic curve to binary data. This logistic curve can be interpreted as the probability associated with each outcome across independent variable values. Logistic regression assumes that the relationship between the natural log of these probabilities (when expressed as odds) and your predictor variable is linear.


2.No Outliers
The variables that you care about must not contain outliers. Logistic Regression is sensitive to outliers, or data points that have unusually large or small values. You can tell if your variables have outliers by plotting them and observing if any points are far from all other points.


3.Independence
Each of your observations (data points) should be independent. This means that each value of your variables doesn’t “depend” on any of the others. For example, this assumption is usually violated when there are multiple data points over time from the same unit of observation (e.g. subject/participant/customer/store), because the data points from the same unit of observation are likely to be related or affect one another.

If your data have repeated measures over time from the same units of observation, you should use Mixed Effects Logistic Regression.


4.No Multicollinearity
Multicollinearity refers to the scenario when two or more of the independent variables are substantially correlated amongst each other. When multicollinearity is present, the regression coefficients and statistical significance become unstable and less trustworthy, though it doesn’t affect how well the model fits the data per se.


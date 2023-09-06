def compute_CoefficientModel(x_train, y_train):
    length = len(x_train)
    
    # Calculate the mean of X and Y
    mean_x = sum(x_train) / length
    mean_y = sum(y_train) / length

    # Compute the slope and intercept/bias

    numerator = sum((x_train[i] - mean_x) * (y_train[i] - mean_y) for i in range(length))
    denominator = sum((x_train[i] - mean_x)**2 for i in range(length))

    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    return [slope, intercept]

def predict_LableModel(x_test, coefficient):
    slope = coefficient[0]
    intercept = coefficient[-1]

    return x_test * slope + intercept



def compute_MSE(y_test, y_pred):
    length = len(y_pred)

    # Sum square error
    sae = sum((y_pred[i] - y_test[i])**2 for i in range(length))
    # Mean square error
    mse = sae / length

    return mse


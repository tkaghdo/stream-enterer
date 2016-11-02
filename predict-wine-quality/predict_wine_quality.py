__author__ = 'Tamby Kaghdo'
"""
Predict wine quality
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import sys

# *** Begin Functions ***
def calculate_correlations(df,target_column):
    """
    Used to create a series of correlations
    :param df: pandas data frame
    :param target_column: the column running the correlations against
    :return: a series with correlations against target_column
    """
    corr_series = df.corr()
    corr_series = corr_series[target_column]
    return corr_series

def create_train_test(df):
    """
    breaks the panadas data frame into train and test data sets. 80/20
    :param df: the data frame to be broken up
    :return: train and test data frames
    """
    shuffled_index = np.random.permutation(df.index)
    shuffled_df = df.loc[shuffled_index]
    #train is 80% of the shuffled list
    train_length = int(np.ceil(len(shuffled_index) * 0.80))
    train_df = shuffled_df[0:train_length]
    test_df = shuffled_df[train_length:len(shuffled_df)]
    return train_df, test_df


def create_predictions_model(train_df, test_df,features, target):
    """
    Fits the model and create predictions
    :param train_df: the train data frame
    :param test_df: the test data frame
    :param features: the independent variables that are used to fit the X part of the model
    :param target: the dependent variable to is used to fit the Y part of the model
    :return: a list of predictions and the fit model
    """
    model = LinearRegression()
    model.fit(train_df[features], train_df[target])
    predictions = model.predict(test_df[features])
    predictions = [int(x) for x in predictions]
    return predictions, model

def output_prediction(df, predictions, file_location):
    """
    Used to create an output with the predictions added to a file
    :param df: the target data frame
    :param predictions: list of predictions
    :param file_location: the file that will hold the result of the data combination
    """
    predictions_series = pd.Series(predictions)
    df["predictions"] = predictions_series.values
    try:
        df.to_csv(file_location)
        print("prediction file saved to: {0}".format(file_location))
    except:
        print("Exception while trying to save file: {0}".format(file_location))

# *** End Functions ***
def main():
    try:
        red_wine_df = pd.read_csv("data/winequality-red.csv", sep=";")
        white_wine_df = pd.read_csv("data/winequality-white.csv", sep=";")
    except:
        print("Error opening files")
        sys.exit(1)

    print("CORRELATIONS IN RED WINE DATE")
    print(calculate_correlations(red_wine_df,"quality"))
    # *** work on red wine first ***
    #drop columns with low correlations
    modified_red_wine_df = red_wine_df[["fixed acidity", "volatile acidity", "citric acid", "chlorides", \
                                       "total sulfur dioxide", "density", \
                                       "sulphates", "alcohol", "quality"]]
    #low_corr_columns = ["residual sugar", "free sulfur dioxide", "pH"]
    #modified_red_wine_df.drop(low_corr_columns, axis=1, inplace=True)

    #create train and test data sets
    train_df, test_df = create_train_test(modified_red_wine_df)

    #create red wine Linear Regression model
    features = ["fixed acidity", "volatile acidity", "citric acid", "chlorides", "total sulfur dioxide", "density", "sulphates", "alcohol"]
    target = "quality"
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #calculate the Mean Absolute Error (MAE), Mean Absolute Error (MSE) and model score
    mae = float(sum([abs(x-y) for x,y in zip(predictions,test_df[target].tolist())])) / len(predictions)
    mse = mean_squared_error(test_df[target].tolist(), predictions)
    print("Mean Absolute Error (MAE) (red wine): {0}".format(mae))
    print("Mean Squared Error (MSE) (red wine): {0}".format(mse))
    print("Model Score: {0} (red wine)").format(model.score(train_df[features], train_df[target]))

    #output predictions to file for visual confirmation
    output_prediction(test_df, predictions, "data/test_red_wine_with_predictions.csv")
    # *** End red wine section ***

    # *** work on white wine ***
    print("CORRELATIONS IN WHITE WINE DATA")
    print(calculate_correlations(white_wine_df,"quality"))
    modified_white_wine_df = white_wine_df[["fixed acidity", "volatile acidity", "residual sugar", "chlorides", \
                                           "total sulfur dioxide", "density", "alcohol","quality"]]
    #low_corr_columns = ["citric acid", "free sulfur dioxide", "pH", "sulphates"]
    #modified_white_wine_df.drop(low_corr_columns, axis=1, inplace=True)

    #create train and test data sets
    train_df, test_df = create_train_test(modified_white_wine_df)

    #create white wine Linear Regression model
    features = ["fixed acidity", "volatile acidity", "residual sugar", "chlorides", "total sulfur dioxide", "density", "alcohol"]
    target = "quality"
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #calculate the Mean Absolute Error (MAE), Mean Absolute Error (MSE) and model score
    mae = float(sum([abs(x-y) for x,y in zip(predictions,test_df[target].tolist())])) / len(predictions)
    mse = mean_squared_error(test_df[target].tolist(), predictions)
    print("Mean Absolute Error (MAE) (white wine): {0}".format(mae))
    print("Mean Squared Error (MSE) (white wine): {0}".format(mse))
    print("Model Score: {0} (white wine)").format(model.score(train_df[features], train_df[target]))

    #output predictions to file for visual confirmation
    output_prediction(test_df, predictions, "data/test_white_wine_with_predictions.csv")
    # *** End white wine section ***

    #create predictions for the combined data sets
    wine_df = pd.concat([red_wine_df, white_wine_df], ignore_index=True)
    #create train and test data sets
    train_df, test_df = create_train_test(wine_df)

    #create white wine Linear Regression model
    features = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]
    target = "quality"
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #calculate the Mean Absolute Error (MAE), Mean Absolute Error (MSE) and model score
    mae = float(sum([abs(x-y) for x,y in zip(predictions,test_df[target].tolist())])) / len(predictions)
    mse = mean_squared_error(test_df[target].tolist(), predictions)
    print("Mean Absolute Error (MAE) (all sets): {0}".format(mae))
    print("Mean Squared Error (MSE) (all sets): {0}".format(mse))
    print("Model Score: {0} (all sets)").format(model.score(train_df[features], train_df[target]))

    #output predictions to file for visual confirmation
    output_prediction(test_df, predictions, "data/test_wine_with_predictions.csv")

if __name__ == "__main__":
    sys.exit(0 if main() else 1)

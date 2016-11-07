__author__ = 'Tamby Kaghdo'

"""
the purpose of this program is to predict the values of motor_UPDRS and total_UPDRS
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# *** Begin Functions ***
def remove_nan(df):
    pass

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
    predictions = [float(x) for x in predictions]
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
        study_df = pd.read_csv("data/parkinsons_updrs.data", sep=",")
    except:
        print("Error opening files")
        sys.exit(1)

    print(study_df.head(5))

    #check if any of the rows have a NaN
    if study_df.isnull().values.any() == True:
        remove_nan(study_df)

    print(study_df.head(5))

    #generate frequencies plot by age and sex
    fig = plt.figure(figsize=(16,8))
    fig.suptitle("Age & Gender Frequencies", fontsize=14)
    ax1 = fig.add_subplot(1,2,1)
    ax1.set_xlim([min(study_df["age"]),max(study_df["age"])])
    ax1.set_xlabel("Age")
    ax1 = study_df["age"].hist(color="cornflowerblue")

    ax2 = fig.add_subplot(1,2,2)
    ax2.set_xlim([min(study_df["sex"]),max(study_df["sex"])])
    ax2.set_xlabel("Gender")
    ax2 = study_df["sex"].hist(color="seagreen")

    plt.show()

    #TODO: statistics for all numeric measures

    features = ['age','sex','test_time','Jitter(%)','Jitter(Abs)','Jitter:RAP','Jitter:PPQ5','Jitter:DDP','Shimmer', \
                'Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','NHR','HNR','RPDE','DFA','PPE']
    target = "motor_UPDRS"

    #calculate correlations to motor_UPDRS
    print("CORRELATIONS WITH motor_UPDRS")
    print(calculate_correlations(study_df,target))

    #create train and test data sets
    train_df, test_df = create_train_test(study_df)

    #create linear regression model for motor_UPDRS
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #calculate the Mean Absolute Error (MAE), Mean Absolute Error (MSE) and model score
    mae = float(sum([abs(x-y) for x,y in zip(predictions,test_df[target].tolist())])) / len(predictions)
    mse = mean_squared_error(test_df[target].tolist(), predictions)
    print("Mean Absolute Error (MAE) (motor_UPDRS): {0}".format(mae))
    print("Mean Squared Error (MSE) (motor_UPDRS): {0}".format(mse))
    print("Model Score: {0} (motor_UPDRS)").format(model.score(train_df[features], train_df[target]))

    #output predictions to file for visual confirmation
    output_prediction(test_df, predictions, "data/test_motor_UPDRS_with_predictions.csv")

    #lets look at total_UPDRS
    target = "total_UPDRS"

    #calculate correlations to total_UPDRS
    print("CORRELATIONS WITH motor_UPDRS")
    print(calculate_correlations(study_df,target))

    #create train and test data sets
    train_df, test_df = create_train_test(study_df)
    #create linear regression model for total_UPDRS
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #create linear regression model for motor_UPDRS
    predictions, model = create_predictions_model(train_df, test_df, features, target)

    #calculate the Mean Absolute Error (MAE), Mean Absolute Error (MSE) and model score
    mae = float(sum([abs(x-y) for x,y in zip(predictions,test_df[target].tolist())])) / len(predictions)
    mse = mean_squared_error(test_df[target].tolist(), predictions)
    print("Mean Absolute Error (MAE) (total_UPDRS): {0}".format(mae))
    print("Mean Squared Error (MSE) (total_UPDRS): {0}".format(mse))
    print("Model Score: {0} (total_UPDRS)").format(model.score(train_df[features], train_df[target]))

    #output predictions to file for visual confirmation
    output_prediction(test_df, predictions, "data/test_total_UPDRS_with_predictions.csv")

if __name__ == "__main__":
    sys.exit(0 if main() else 1)


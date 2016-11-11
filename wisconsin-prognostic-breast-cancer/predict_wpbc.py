__author__ = 'Tamby Kaghdo'

"""
this script is used to generate Logistic Regression (classification) model in order to predict the breast cancer prognosis
"""

import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from optparse import OptionParser

# *** FUNCTIONS ***
def calculate_confusion_matrix_values(df, predicted_indicator, actual_indicator):
    """
    calculates true positive, true negative, false positive, false negative
    :param df: a data frame with both predicted and actual values
    :param predicted_indicator: values are 0 or 1
    :param actual_indicator: values are 0 or 1
    :return: a confusion matrix value: true positive, true negative, false positive, false negative
    """
    df = df[df["predicted_label"] == predicted_indicator]
    df = df[df["outcome_integer"] == actual_indicator]
    return df.shape[0]

def calculate_sensitivity_specificity(wpbc_df):
    true_positives = calculate_confusion_matrix_values(wpbc_df,1,1)
    true_negatives = calculate_confusion_matrix_values(wpbc_df,0,0)
    false_negatives = calculate_confusion_matrix_values(wpbc_df,0,1)
    false_positives = calculate_confusion_matrix_values(wpbc_df,1,0)
    sensitivity = float(true_positives) / float((true_positives + false_negatives))
    specificity = float(true_negatives) / float((false_positives + true_negatives))
    return true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity

def model_on_whole_data_set(wpbc_df, features):
    # *** lets fit the model on the whole list (not dividing the data into train and test data sets) ***
    #create a logistic regression model
    model = LogisticRegression()
    model.fit(wpbc_df[features], wpbc_df["outcome_integer"])

    outcome_prediction = model.predict(wpbc_df[features])
    wpbc_df["predicted_label"] = outcome_prediction
    print(wpbc_df["predicted_label"].value_counts())

    #calculate accuracy of the model
    matches = wpbc_df["predicted_label"] == wpbc_df["outcome_integer"]
    correct_predictions = wpbc_df[matches]
    print(correct_predictions.head())
    accuracy = float(len(correct_predictions)) / float(len(wpbc_df))
    print("Accuracy: {0}".format(accuracy))

    #Sensitivity and Specificity
    true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity = calculate_sensitivity_specificity(wpbc_df)

    print("True Positive: {0}".format(true_positives))
    print("True Negative: {0}".format(true_negatives))
    print("False Negative: {0}".format(false_negatives))
    print("False Positive: {0}".format(false_positives))
    print("Sensitivity: {0}".format(sensitivity))
    print("Specificity: {0}".format(specificity))

def model_using_holdout_validation(wpbc_df, features):
    #create train and test data sets
    train_df, test_df = create_train_test(wpbc_df)

    #create a logistic regression model
    model = LogisticRegression()
    model.fit(train_df[features], train_df["outcome_integer"])

    predictions = model.predict(test_df[features])
    test_df["predicted_label"] = predictions

    matches = test_df["predicted_label"] == test_df["outcome_integer"]
    correct_predictions = test_df[matches]
    accuracy = float(len(correct_predictions)) / float(len(test_df))
    print("Accuracy: {0}".format(accuracy))

    #Sensitivity and Specificity
    true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity = calculate_sensitivity_specificity(test_df)
    print("True Positive: {0}".format(true_positives))
    print("True Negative: {0}".format(true_negatives))
    print("False Negative: {0}".format(false_negatives))
    print("False Positive: {0}".format(false_positives))
    print("Sensitivity: {0}".format(sensitivity))
    print("Specificity: {0}".format(specificity))

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

def prepare_df(file):
    try:
        wpbc_df = pd.read_csv(file, sep=",")
    except:
        print("Error opening file")
        sys.exit(1)
    print("there are {0} rows in the data set".format(len(wpbc_df)))
    #clean up: some rows have '?' in lymph_node_status. Lets see how many rows are there with '?'
    temp_df = wpbc_df[wpbc_df["lymph_node_status"] == '?']
    print("there are {0} rows with '?' in lymph_node_status column".format(len(temp_df)))
    #there were only 4 rows where lymph_node_status = '?'. So I will delete these 4 rows
    wpbc_df = wpbc_df[wpbc_df["lymph_node_status"] != '?']
    print("there are now {0} rows in the data set".format(len(wpbc_df)))
    #create an integer equivalent of 'outcome'
    wpbc_df["outcome_integer"] = [0 if x == "N" else 1 for x in wpbc_df["outcome"]]
    return wpbc_df

# *** END FUNCTIONS

def main():
    status = True
    use = '''Usage: %prog model_method
    model_method: "ALL", "HOLDOUT"
    '''
    parser = OptionParser(usage=use)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
        status = False
    else:
        features = ['recurrence_time', 'cell_radius','cell_texture','cell_perimeter','cell_area','cell_smoothness','cell_compactness', \
                    'cell_concave_points','cell_symmetry','cell_fractal_dimension','cell_11','cell_12','cell_13','cell_14','cell_15', \
                    'cell_16','cell_17','cell_18','cell_19','cell_20','cell_21','cell_22','cell_23','cell_24','cell_25','cell_26','cell_27', \
                    'cell_28','cell_29','cell_30_cell_31','cell_32','tumor_size','lymph_node_status']

        if sys.argv[1].upper() == "ALL":
            wpbc_df = prepare_df("data/wpbc.data")
            model_on_whole_data_set(wpbc_df, features)
        elif sys.argv[1].upper() == "HOLDOUT":
            wpbc_df = prepare_df("data/wpbc.data")
            model_using_holdout_validation(wpbc_df, features)
        else:
            parser.error("incorrect option")
            status = False
    return status

if __name__ == "__main__":
    sys.exit(0 if main() else 1)

    #TODO: ROC Curve
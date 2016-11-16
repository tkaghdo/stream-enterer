__author__ = 'Tamby Kaghdo'

"""
this script is used to generate Logistic Regression (classification) model in order to predict the breast cancer prognosis
"""

import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from optparse import OptionParser
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import roc_auc_score

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

def model_performance_metrics(wpbc_df):
    """
    calculates model performance
    :param wpbc_df: data frame with predicted and actual columns
    :return: true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity, fall_out_rate
    """
    true_positives = calculate_confusion_matrix_values(wpbc_df,1,1)
    true_negatives = calculate_confusion_matrix_values(wpbc_df,0,0)
    false_negatives = calculate_confusion_matrix_values(wpbc_df,0,1)
    false_positives = calculate_confusion_matrix_values(wpbc_df,1,0)
    sensitivity = float(true_positives) / float(true_positives + false_negatives)
    specificity = float(true_negatives) / float(false_positives + true_negatives)
    fall_out_rate = float(false_positives) / float(false_positives + true_negatives)
    return true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity, fall_out_rate

def model_on_whole_data_set(wpbc_df, features):
    """
    fit the model on the whole list (not dividing the data into train and test data sets)
    :param wpbc_df: data frame that will be used to create the model
    :param features: the independent variables used to generate the model
    :return: None
    """
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
    true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity, fall_out_rate = model_performance_metrics(wpbc_df)

    print("True Positive: {0}".format(true_positives))
    print("True Negative: {0}".format(true_negatives))
    print("False Negative: {0}".format(false_negatives))
    print("False Positive: {0}".format(false_positives))
    print("Sensitivity: {0}".format(sensitivity))
    print("Specificity: {0}".format(specificity))
    print("Fall Out Rate: {0}".format(fall_out_rate))

    #ROC
    probabilities = model.predict_proba(wpbc_df[features])
    fpr, tpr, thresholds = metrics.roc_curve(wpbc_df["outcome_integer"], probabilities[:,1])
    plt.plot(fpr,tpr)
    plt.show()

    #AUC
    auc_score = roc_auc_score(wpbc_df["outcome_integer"],probabilities[:,1])
    print("AUC Score: {0}".format(auc_score))

def model_using_holdout_validation(wpbc_df, features):
    """
    fit model on a train and predict a test data frame
    :param wpbc_df: data frame that will be used to create the model
    :param features: the independent variables used to generate the model
    :return: None
    """
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
    true_positives, true_negatives, false_negatives, false_positives, sensitivity, specificity, fall_out_rate = model_performance_metrics(test_df)
    print("True Positive: {0}".format(true_positives))
    print("True Negative: {0}".format(true_negatives))
    print("False Negative: {0}".format(false_negatives))
    print("False Positive: {0}".format(false_positives))
    print("Sensitivity: {0}".format(sensitivity))
    print("Specificity: {0}".format(specificity))
    print("Fall Out Rate: {0}".format(fall_out_rate))

    #ROC
    probabilities = model.predict_proba(test_df[features])
    fpr, tpr, thresholds = metrics.roc_curve(test_df["outcome_integer"], probabilities[:,1])
    plt.plot(fpr,tpr)
    plt.show()

    #AUC
    auc_score = roc_auc_score(test_df["outcome_integer"],probabilities[:,1])
    print("AUC Score: {0}".format(auc_score))

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
    """
    cleans up the input file
    :param file: the input file
    :return: data frame of the cleaned and modified data
    """
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

def get_data_with_folds(wpbc_df, folds):
    rows_per_fold = int(np.ceil(float(len(wpbc_df)) / float(folds)))
    print("Rows Per Fold: {0}".format(rows_per_fold))

    #shuffle the data frame
    shuffled_index = np.random.permutation(wpbc_df.index)
    shuffled_admissions = wpbc_df.loc[shuffled_index]
    wpbc_df = shuffled_admissions.reset_index()
    start = 0
    end = rows_per_fold
    for i in range(1,folds+1):
        wpbc_df.ix[start:end, "fold"] = i
        start = end + 1
        end = end + rows_per_fold + 1

    wpbc_df["fold"] = wpbc_df["fold"].astype('int')
    return wpbc_df

def train_and_test_kfold(df, features, lst):
    accuracies_lst = []
    for i in lst:
        model = LogisticRegression()
        train = df[df["fold"] != i]
        test = df[df["fold"] == i]
        model.fit(train[features],train["outcome_integer"])
        labels = model.predict(test[features])
        test["predicted_label"] = labels
        correct_predictions = test[test["predicted_label"] == test["outcome_integer"]]
        accuracies_lst.append(float(len(correct_predictions))/float(len(test)))
    return accuracies_lst



def model_using_kfold_cross_validation(wpbc_df, features, folds):
    wpbc_df = get_data_with_folds(wpbc_df, folds)
    accuracies = train_and_test_kfold(wpbc_df, features, [1, 2, 3, 4, 5])
    average_accuracy = np.mean(accuracies)
    print("Average Accuracy using my kfold cross validation: {0}".format(average_accuracy))

# *** END FUNCTIONS

def main():
    """
    the main function handles command line inputs and create the model/predictions based on the input parameter
    :arg1: "ALL" to run the model against the whole data. "HOLDOUT" to do an 80/20 holdout validation and run the model on the 80 and test on the 20
    :return: status 1 if error, 0 if success
    """
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
        elif sys.argv[1].upper() == "KFOLD":
            # implement my own k fold cross validation
            wpbc_df = prepare_df("data/wpbc.data")
            model_using_kfold_cross_validation(wpbc_df, features, 5)
        else:
            parser.error("incorrect option")
            status = False
    return status

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
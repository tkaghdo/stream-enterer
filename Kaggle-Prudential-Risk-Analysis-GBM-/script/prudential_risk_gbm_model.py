__author__ = 'Tamby Kaghdo'

# general modules for Data science
import numpy as np
import pandas as pd
import random

# plotting module
import matplotlib as plt


# machine learning platform and model evaluation
import h2o
from sklearn import metrics
from collections import Counter

def main():

    # initialization of H2O module
    h2o.init()

    # Define file path
    file_path = 'C:\\workspace\DataScience Github\\Kaggle Prudential Risk Analysis\\data\\train.csv'

    # load data
    params_load_data = {'path': file_path,
                        'header': 1,
                        'sep': ','}
    data_hex = h2o.import_file(**params_load_data)

    # count number of records
    num_records = data_hex.nrow

    # print the number with comment
    print 'Records number in this data set is : ' + str(num_records)

    # --- responce variable
    response = unicode('Response')

    features = ['Product_Info_1', 'Product_Info_2', 'Product_Info_3', 'Product_Info_5', 'Product_Info_6',
                'Product_Info_7', 'Employment_Info_2', 'Employment_Info_3', 'Employment_Info_5', 'InsuredInfo_1',
                'InsuredInfo_2', 'InsuredInfo_3', 'InsuredInfo_4', 'InsuredInfo_5', 'InsuredInfo_6', 'InsuredInfo_7',
                'Insurance_History_1', 'Insurance_History_2', 'Insurance_History_3', 'Insurance_History_4',
                'Insurance_History_7', 'Insurance_History_8', 'Insurance_History_9', 'Family_Hist_1',
                'Medical_History_2', 'Medical_History_3', 'Medical_History_4', 'Medical_History_5', 'Medical_History_6',
                'Medical_History_7', 'Medical_History_8', 'Medical_History_9', 'Medical_History_10',
                'Medical_History_11', 'Medical_History_12', 'Medical_History_13', 'Medical_History_14',
                'Medical_History_16', 'Medical_History_17', 'Medical_History_18', 'Medical_History_19',
                'Medical_History_20', 'Medical_History_21', 'Medical_History_22', 'Medical_History_23',
                'Medical_History_25', 'Medical_History_26', 'Medical_History_27', 'Medical_History_28',
                'Medical_History_29', 'Medical_History_30', 'Medical_History_31', 'Medical_History_33',
                'Medical_History_34', 'Medical_History_35', 'Medical_History_36', 'Medical_History_37',
                'Medical_History_38', 'Medical_History_39', 'Medical_History_40', 'Medical_History_41', 'Response']

    # find index of response varaible
    for idx, feature in enumerate(features):
        if feature == response:
            idx_response = idx

    # convert data type to factor
    data_hex[response] = data_hex[response].asfactor()

    # a vector with uniformly distributed numbers between 0 and 1
    random_idx = data_hex[idx_response].runif(seed=1234)

    # split the data set into training and testing data sets
    train_hex = data_hex[random_idx < 0.7]
    test_hex = data_hex[random_idx >= 0.7]

    # a vector with uniformly distributed numbers between 0 and 1
    random_idx = train_hex[idx_response].runif()

    # split the data set into two holdout sets
    train_holdout_hex       = train_hex[ random_idx < 0.8]
    validation_holdout_hex  = train_hex[ random_idx >= 0.8]

    train_holdout_df = population(train_holdout_hex, num_records)
    validation_holdout_df  = population(validation_holdout_hex, num_records)

    # range of grid search
    range_ntrees   = np.arange(500, 5000, 100)
    range_depth    = np.arange(1, 2, 1)
    range_min_rows = np.arange(10, 21, 1)

    #--- sampling number
    num_models = 10

    # define empty list to store the models
    gbm_models = []

    # loop over
    for id_model in range(num_models):

        # choose mode parameters
        ntree = random.sample(range_ntrees, 1)[0]
        depth = random.sample(range_depth, 1)[0]
        min_rows = random.sample(range_min_rows, 1)[0]

        # build model
        params_model = {'x': features,
                        'y': response,
                        'training_frame': train_holdout_hex,
                        'validation_frame': validation_holdout_hex,
                        'ntrees': ntree,
                        'max_depth': depth,
                        'learn_rate': 0.005
                        }
        gbm_model = h2o.gbm(**params_model)

        # store model
        gbm_models.append(gbm_model)

    best_acc = 0
    best_acc_id = 0
    # loop
    model_counter = 0
    for id_model, model in enumerate(gbm_models):
        model_counter += 1
        # predicted and actual values (in H2O)
        y_predict = model.predict(validation_holdout_hex)[0]
        y_actual  = validation_holdout_hex[response]

        # transform values into Pandas
        y_predict_array = y_predict.as_data_frame()
        y_actual_array  = y_actual.as_data_frame()
        #remove headers
        y_predict_array[0].remove('predict')
        y_actual_array[0].remove('Response')

        #convert
        y_actual_array_int = []
        for i in y_actual_array[0]:
            y_actual_array_int.append(int(round(float(i),1)))

        y_predict_array_int = []
        for i in y_predict_array[0]:
            y_predict_array_int.append(int(round(float(i),1)))

        accuracy = metrics.accuracy_score(y_actual_array_int, y_predict_array_int)
        print 'Accuracy for model {0} is {1}'.format(model_counter,float(accuracy))
        # compare with best_acc and index
        if accuracy > best_acc:
            best_acc = accuracy
            best_acc_id = id_model

    # store the best model
    best_model = gbm_models[best_acc_id]

    # print result
    print 'Best Accuracy is {0}'.format(best_acc)

    list_model_params = list(best_model.params.keys())
    bmps = best_model.params.items()

    best_ntree    = bmps[list_model_params.index('ntrees')][1]['actual']
    best_depth    = bmps[list_model_params.index('max_depth')][1]['actual']
    best_min_rows = bmps[list_model_params.index('min_rows')] [1]['actual']

    params_best_model = {'x': features,
                     'y': response,
                     'training_frame': train_hex,
                     'validation_frame': test_hex,
                     'ntrees': best_ntree,
                     'max_depth': best_depth,
                     'min_rows': best_min_rows,
                     'learn_rate': 0.005
                     }
    rebuild_gbm_model = h2o.gbm(**params_best_model)

    #TODO: load model
    #

    print rebuild_gbm_model.model_performance(train_hex)

    # predicted and actual values (in H2O)
    y_predict = rebuild_gbm_model.predict(test_hex)[0]
    y_predict_lst = y_predict.as_data_frame()
    y_predict_lst[0].remove('predict')

    #TODO: make this dynamic
    idx_response = 127
    y_actual  = test_hex[idx_response]
    y_actual_lst = y_actual.as_data_frame()
    y_actual_lst[0].remove('Response')

    y_actual_lst_int = []
    for i in y_actual_lst[0]:
        y_actual_lst_int.append(int(round(float(i),1)))

    y_predict_lst_int = []
    for i in y_predict_lst[0]:
        y_predict_lst_int.append(int(round(float(i),1)))

    accuracy_rebuild = metrics.accuracy_score(y_actual_lst_int, y_predict_lst_int)

    # print out the accuracy
    print accuracy_rebuild

    file_path = 'C:\\workspace\\DataScience\\models\\final_gbm_model'

    params_save = {'model': rebuild_gbm_model,
                   'path' : file_path,
                   'force': True}
    h2o.save_model(**params_save)

    #Create submission file
    print '++++++++++++'
    #print rebuild_gbm_model.predict(train_hex)
    input_file = 'C:\\workspace\\DataScience Github\\Kaggle Prudential Risk Analysis\data\\test.csv'
    output_file = 'C:\workspace\DataScience Github\Kaggle Prudential Risk Analysis\data\\test_prediction.csv'
    create_submission_file(rebuild_gbm_model,input_file,output_file)
    print '+++++++++++'


    #END MAIN

def create_submission_file(model, input_file, output_file):
    # load data
    params_load_data = {'path': input_file,
                        'header': 1,
                        'sep': ','}
    data_hex = h2o.import_file(**params_load_data)
    num_records = data_hex.nrow
    print 'Records number in this data set is : ' + str(num_records)

    y_predict = model.predict(data_hex)[0]

    data_hex['predicted']=y_predict
    df = data_hex.as_data_frame(use_pandas=True)
    df.to_csv('C:\\workspace\DataScience Github\\Kaggle Prudential Risk Analysis\\data\\submission_file.csv', sep=',')


def response_keys_values(df, indx):
    temp_df = df
    keys_lst = Counter(temp_df[indx]).keys()
    values_lst = Counter(temp_df[indx]).values()
    del temp_df

    return keys_lst, values_lst

def get_response_values_perctages(num_records, response_keys, response_values):
    d = {}
    if (len(response_keys) != len(response_values)):
        print 'ERROR'
    else:
        # remove 'Response'
        response_keys.pop(len(response_keys) - 1)
        response_values.pop(len(response_values) - 1)

        i = 0
        for key in response_keys:
            # calculate the percentage of each response value
            d[key] = float(response_values[i]) / float(num_records)
            i += 1
    #d.pop('label')
    return d

def population(h2o_data_set,num_records):
    # transform h2o data set to pandas data frame
    temp_df = h2o_data_set.as_data_frame()
    #####
    response_keys, response_values = response_keys_values(temp_df, 0)
    response_perc_dict = get_response_values_perctages(num_records, response_keys, response_values)
    #####
    return response_perc_dict


if __name__ == '__main__':
    main()

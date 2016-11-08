__author__ = 'Tamby Kaghdo'

"""
this script is used to generate Logistic Regression (classification) model in order to predict the breast cancer prognosis
"""

import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression

def main():
    try:
        wpbc_df = pd.read_csv("data/wpbc.data", sep=",")
    except:
        print("Error opening file")
        sys.exit(1)

    print("there are {0} rows in the data set".format(len(wpbc_df)))
    #print(wpbc_df.head(1))
    #clean up: some rows have '?' in lymph_node_status. Lets see how many rows are there with '?'
    temp_df = wpbc_df[wpbc_df["lymph_node_status"] == '?']
    print("there are {0} rows with '?' in lymph_node_status column".format(len(temp_df)))

    #there were only 4 rows where lymph_node_status = '?'. So I will delete these 4 rows
    wpbc_df = wpbc_df[wpbc_df["lymph_node_status"] != '?']
    print("there are now {0} rows in the data set".format(len(wpbc_df)))


    # *** lets fit the model on the whole list (not dividing the data into train and test data sets) ***

    features = ['recurrence_time', 'cell_radius','cell_texture','cell_perimeter','cell_area','cell_smoothness','cell_compactness', \
                'cell_concave_points','cell_symmetry','cell_fractal_dimension','cell_11','cell_12','cell_13','cell_14','cell_15', \
                'cell_16','cell_17','cell_18','cell_19','cell_20','cell_21','cell_22','cell_23','cell_24','cell_25','cell_26','cell_27', \
                'cell_28','cell_29','cell_30_cell_31','cell_32','tumor_size','lymph_node_status']

    #create an integer equivalent of 'outcome'
    #target = "outcome_integer"
    wpbc_df["outcome_integer"] = [0 if x == "N" else 1 for x in wpbc_df["outcome"]]

    print(wpbc_df.head(5))

    model = LogisticRegression()
    model.fit(wpbc_df[features], wpbc_df["outcome_integer"])

    outcome_prediction = model.predict(wpbc_df[features])
    #admissions["predicted_label"] = labels
    #print(admissions["predicted_label"].value_counts())
    #print(admissions.head(5))

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
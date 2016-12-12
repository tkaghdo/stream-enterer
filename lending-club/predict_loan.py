#machine learning model that can accurately predict if a borrower will pay off their loan on time or not
#target is loan_status

#clean up data

import pandas as pd
import numpy as np

loans_2007 = pd.read_csv('./data/LoanStats3a.csv', skiprows=1)
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count, axis=1)
loans_2007 = loans_2007.drop(['desc', 'url'],axis=1)
loans_2007.to_csv('./data/loans_2007.csv', index=False)

#read into pandas
loans_2007 = pd.read_csv("./data/loans_2007.csv")
#print(loans_2007.head(1))
#print(len(loans_2007))

#drop some columns
columns_to_drop = ["id", "member_id", "funded_amnt", "funded_amnt_inv", "grade", \
                   "sub_grade", "emp_title", "issue_d", "zip_code", "out_prncp", "out_prncp_inv", \
                   "total_pymnt", "total_pymnt_inv", "total_rec_prncp", "total_rec_int", "total_rec_late_fee", \
                   "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"]
loans_2007 = loans_2007.drop(columns_to_drop, axis=1)


print(loans_2007['loan_status'].value_counts())


#we're interesting in being able to predict which of these 2 values a loan will fall under,
# we can treat the problem as a binary classification one. Let's remove all the loans that don't contain either
# Fully Paid and Charged Off as the loan's status and then transform the Fully Paid values to 1 for the positive case
# and the Charged Off values to 0 for the negative case
loans_2007 = loans_2007[(loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")]

dict = {
    "loan_status": {
        "Fully Paid": 1,
        "Charged Off": 0
    }
}

loans_2007 = loans_2007.replace(dict)


#Remove Single Value Columns
orig_columns = loans_2007.columns
drop_columns = []
for col in orig_columns:
    col_series = loans_2007[col].dropna().unique()
    if len(col_series) == 1:
        drop_columns.append(col)
loans_2007 = loans_2007.drop(drop_columns, axis=1)
print(drop_columns)

#save the filtered data frame to csv
loans_2007.to_csv("./data/filtered_loans_2007.csv" , sep=",")

loans = loans_2007

#return the number of null values in each column
null_counts = loans.isnull().sum()
print(null_counts)

#remove columns entirely where more than 1% of the rows for that column contain a null value
#In addition, we'll remove the remaining rows containing null values
loans = loans.drop("pub_rec_bankruptcies", axis=1)
loans = loans.dropna(axis=0)
print(loans.dtypes.value_counts())

#convert string columns to numerical
object_columns_df = loans.select_dtypes(include=["object"]) #get string columns
print(object_columns_df.head(1))

# what are the unique values in the string columns
cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']
for c in cols:
    print(c)
    print(loans[c].value_counts())
    print("---------    ")

#let's look at the unique value counts for the purpose and title columns to understand which column we want to keep
print(loans["purpose"].value_counts())
print(loans["title"].value_counts())


#used to change emp_length column
mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

loans = loans.drop(["last_credit_pull_d", "addr_state", "title", "earliest_cr_line"], axis=1)
#remove % and convert to float
loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype("float")
loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype("float")
#change emp_length
loans = loans.replace(mapping_dict)

#convert categorical columns to dummy variables
cat_columns = ["home_ownership", "verification_status", "emp_length", "purpose", "term"]
dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_columns, axis=1)


#store the clean data
loans.to_csv("./data/cleaned_loans_2007.csv")

#errors
# Predict that all loans will be paid off on time.
predictions = pd.Series(np.ones(loans.shape[0]))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
predictions = pd.Series(predictions)
features = loans.drop("loan_status", axis=1)
target = loans["loan_status"]
lr.fit(features, target)
predictions = lr.predict(features)


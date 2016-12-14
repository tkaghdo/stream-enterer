## 2. Partititioning the data ##

import pandas as pd

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
admissions = shuffled_admissions.reset_index()
admissions.ix[0:128,"fold"] = 1
admissions.ix[129:257,"fold"] = 2
admissions.ix[258:386,"fold"] = 3
admissions.ix[387:514,"fold"] = 4
admissions.ix[515:644,"fold"] = 5
admissions["fold"] = admissions["fold"].astype('int')
print(admissions.head(5))
print(admissions.tail(5))

## 3. First iteration ##

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
train_iter_one = admissions[admissions["fold"] != 1]
test_iter_one = admissions[admissions["fold"] == 1]
model.fit(train_iter_one[["gpa"]],train_iter_one["actual_label"])
labels = model.predict(test_iter_one[["gpa"]])
test_iter_one["predicted_label"] = labels
match = test_iter_one["actual_label"] == test_iter_one["predicted_label"]
correct_predictions = test_iter_one[match]
iteration_one_accuracy = len(correct_predictions) / len(test_iter_one)

## 4. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]
from sklearn.linear_model import LogisticRegression
def train_and_test(df,lst):
    accuracies_lst = []
    for i in lst:
        model = LogisticRegression()
        train = df[df["fold"] != i]
        test = df[df["fold"] == i]
        model.fit(train[["gpa"]],train["actual_label"])
        labels = model.predict(test[["gpa"]])
        test["predicted_label"] = labels
        correct_predictions = test[test["predicted_label"] == test["actual_label"]]
        accuracies_lst.append(len(correct_predictions)/len(test))
    return accuracies_lst

accuracies = train_and_test(admissions, [1,2,3,4,5])
average_accuracy = np.mean(accuracies)
        

## 5. Sklearn ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

kf = KFold(len(admissions), 5, shuffle=True, random_state=8)
lr = LogisticRegression()
accuracies = cross_val_score(lr,admissions[["gpa"]], admissions["actual_label"], scoring="accuracy", cv=kf)
average_accuracy = np.mean(accuracies)
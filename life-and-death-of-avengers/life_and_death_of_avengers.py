__author__ = 'Tamby Kaghdo'

import pandas as pd
import matplotlib.pyplot as plt

avengers = pd.read_csv("../data/avengers.csv")
print(avengers.head(5))

true_avengers = pd.DataFrame()
plt.show()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"] >= 1960]

def add_deaths(row):
    num_deaths = 0
    if row["Death1"] == "YES":
        num_deaths += 1
    if row["Death2"] == "YES":
        num_deaths += 1
    if row["Death3"] == "YES":
        num_deaths += 1
    if row["Death4"] == "YES":
        num_deaths += 1
    if row["Death5"] == "YES":
        num_deaths += 1

    return num_deaths

true_avengers["Deaths"] = true_avengers.apply(add_deaths, axis=1)
print(true_avengers.head(5))

#Calculate the number of rows where Years since joining is accurate
joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)
print(joined_accuracy_count)

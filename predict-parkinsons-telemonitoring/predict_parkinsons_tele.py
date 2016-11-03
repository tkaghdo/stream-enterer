__author__ = 'Tamby Kaghdo'

"""
the purpose of this program is to predict the values of motor_UPDRS and total_UPDRS
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt

# *** Begin Functions ***
def remove_nan(df):
    pass

# *** End Functions ***

def main():
    study_df = pd.read_csv("data/parkinsons_updrs.data", sep=",")
    print(study_df.head(5))

    #check if any of the rows have a NaN
    if study_df.isnull().values.any() == True:
        remove_nan(study_df)

    #TODO: generate statistics and plot frequencies/scatter plots to understand the data
    #TODO: calculate correlations

    print(study_df.head(5))

    #generate a pivot by sex. I noticed there is a value of 0 for sex so I want to dig deeper into this column
    print("Pivot by sex:")
    print(pd.pivot_table(study_df,index=["sex"]))

    #generate frequencies plot by age and sex
    fig = plt.figure(figsize=(16,8))
    fig.suptitle("Age Frequencies", fontsize=14)
    ax1 = fig.add_subplot(1,2,1)
    ax1.set_xlim([min(study_df["age"]),max(study_df["age"])])
    ax1.set_xlabel("Age")
    ax1 = study_df["age"].hist(color="cornflowerblue")

    plt.show()

if __name__ == "__main__":
    sys.exit(0 if main() else 1)


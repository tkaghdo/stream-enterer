__author__ = 'Tamby Kaghdo'

"""
the purpose of this program is to predict the values of motor_UPDRS and total_UPDRS
"""

import pandas as pd
import sys

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


if __name__ == "__main__":
    sys.exit(0 if main() else 1)


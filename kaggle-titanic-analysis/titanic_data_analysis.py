__author__ = 'Tamby Kaghdo'
"""
This is used to perform data analysis on the Titanic training data on Kaggle
https://www.kaggle.com/c/titanic/data
"""

import pandas as pd
import sys
import matplotlib.pyplot as plt

def missing_data_count(df, column):
    '''
    this function is used to get the number missing data in a pandas data frame
    :param column: data frame column
    :return: number of missing values
    '''

    return df[column].isnull().sum()

def missing_data_percent(df, column):
    '''
    calculates the % to total of missing data
    :param series: data frame column
    :return: % of missing data
    '''
    rows_num = float(len(df[column]))
    missing_values_count = float(df[column].isnull().sum())
    missing_data_percent = missing_values_count / rows_num
    return missing_data_percent

def main():
    '''
    Main function of the program
    :return: status
    '''
    status = True
    from optparse import OptionParser

    use = '''Usage: %prog file
    file: format of file "/dir/file.csv"
    '''
    parser = OptionParser(usage=use)

    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
        status = False
    else:
        #import train data into pandas data frame
        try:
            titanic_train_df = pd.read_csv(sys.argv[1])

        except Exception, e:
            print >> sys.stderr, "FILE DOES NOT EXIST"
            print >> sys.stderr, "EXCEPTION: %s" % str(e)
            sys.exit(1)

        #this is used to remove the columns that have more than a certain percent of missing values in a column
        MISSING_VALUES_MAX_PERCENT = 0.5 # 50%

        #how many rows and in the file?
        print("OVERALL COUNTS")
        print("Number of rows: {0}".format(titanic_train_df.shape[0]))
        print("Number of columns: {0}".format(titanic_train_df.shape[1]))

        #lets look at the first 10 rows
        print("----------")
        print("First 10 rows: ")
        print(titanic_train_df.head(10))

        #let get some basic info
        #print(titanic_train_df.describe())

        #what is the number and percent of missing data in each column?
        columns_with_low_missing_values = []
        columns_with_high_missing_values = []
        print("----------")
        print("MISSING DATA INFO: ")
        for c in titanic_train_df:
            missing_count = missing_data_count(titanic_train_df, c)
            missing_percent = missing_data_percent(titanic_train_df, c)
            print("count of missing values for {0} is {1}. % of missing is {2:.1%}".format(c,missing_count,missing_percent))
            if missing_percent <= MISSING_VALUES_MAX_PERCENT:
                columns_with_low_missing_values.append(c)
            else:
                columns_with_high_missing_values.append(c)

        # do some cleanup
        # remove the columns that has missing values percent more than MISSING_VALUES_MAX_PERCENT
        titanic_train_df_low_missing_values = titanic_train_df[columns_with_low_missing_values]
        print(titanic_train_df_low_missing_values.head(10))

        # what is the frequencies for Sex, Age, Fare, Pclass?
        # create a subplot for all, survived, not survived for each of the above categories
        titanic_train_df_survived = titanic_train_df_low_missing_values[titanic_train_df_low_missing_values["Survived"] == 1]
        print(titanic_train_df_survived.head(10))
        titanic_train_df_not_survived = titanic_train_df_low_missing_values[titanic_train_df_low_missing_values["Survived"] == 0]
        print(titanic_train_df_not_survived.head(10))

        # begin AGE charts
        fig = plt.figure(figsize=(16,8))
        fig.suptitle("Survival Count by Age", fontsize=14)
        ax1 = fig.add_subplot(1,3,1)
        ax1.set_xlim([min(titanic_train_df_low_missing_values["Age"]),max(titanic_train_df_low_missing_values["Age"])])
        ax1.set_xlabel("All Age Freq")
        ax1 = titanic_train_df_low_missing_values["Age"].hist(color="cornflowerblue")

        ax2 = fig.add_subplot(1,3,2)
        ax2.set_xlim([min(titanic_train_df_survived["Age"]),max(titanic_train_df_survived["Age"])])
        ax2.set_xlabel("Survived by Age Freq")
        ax2 = titanic_train_df_survived["Age"].hist(color="seagreen")

        ax3 = fig.add_subplot(1,3,3)
        ax3.set_xlim([min(titanic_train_df_not_survived["Age"]),max(titanic_train_df_not_survived["Age"])])
        ax3.set_xlabel("Not Survived by Age Freq")
        ax3 = titanic_train_df_not_survived["Age"].hist(color="cadetblue")
        # end AGE charts
        #plt.show()
        plt.savefig("survival_count_by_age.png")

        # begin Gender charts
        fig = fig = plt.figure(figsize=(16,8))
        fig.suptitle("Survival Count by Gender", fontsize=14)
        ax1 = fig.add_subplot(1,3,1)
        ax1 = titanic_train_df_low_missing_values.groupby("Sex").size().plot(kind="bar", color="cornflowerblue")
        ax1.set_xlabel("Passenger Count by Gender")

        ax2 = fig.add_subplot(1,3,2)
        ax2 = titanic_train_df_survived.groupby("Sex").size().plot(kind="bar", color="seagreen")
        ax2.set_xlabel("Survived Count by Gender")

        ax3 = fig.add_subplot(1,3,3)
        ax3 = titanic_train_df_not_survived.groupby("Sex").size().plot(kind="bar", color="cadetblue")
        ax3.set_xlabel("Not Survived Count by Gender")

        #plt.show()
        plt.savefig("survival_count_by_gender.png")
        # End Gender charts

        #get some info on the Fare column
        print(titanic_train_df_low_missing_values["Fare"].describe())
        fig = fig = plt.figure(figsize=(16,8))
        fig.suptitle("Fare Frequencies", fontsize=14)
        ax1 = fig.add_subplot(1,1,1)
        ax1.set_xlim([min(titanic_train_df_low_missing_values["Fare"]),max(titanic_train_df_low_missing_values["Fare"])])
        ax1.set_xlabel("Fare Frequencies")
        ax1 = titanic_train_df_low_missing_values["Fare"].hist(color="cornflowerblue")
        #plt.show()
        plt.savefig("fare_frequencies.png")

        #I want to compare the survival rate between passengers who paid less or equal fifty and the ones who paid more
        less_than_or_equal_fifty_survived_df = titanic_train_df_survived[titanic_train_df_survived["Fare"] <= 50]
        print(less_than_or_equal_fifty_survived_df.head(10))
        greater_than_fifty_survived_df = titanic_train_df_survived[titanic_train_df_survived["Fare"] > 50]
        print(greater_than_fifty_survived_df.head(10))

        total_number_of_survived = titanic_train_df_survived.shape[0]
        print("Total Passengers Survived: {0}".format(total_number_of_survived))
        print("Total Passengers Survived (Paid 50 or less): {0} ({1: .1%})".format(less_than_or_equal_fifty_survived_df.shape[0],float(less_than_or_equal_fifty_survived_df.shape[0])/float(total_number_of_survived)))
        print("Total Passengers Survived (Paid more than 50): {0} ({1: .1%})".format(greater_than_fifty_survived_df.shape[0],float(greater_than_fifty_survived_df.shape[0])/float(total_number_of_survived)))

    return status

if __name__ == "__main__":
    # call main
    sys.exit(0 if main() else 1)
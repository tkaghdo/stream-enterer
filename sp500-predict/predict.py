__author__ = 'Tamby Kaghdo'

"""
Predict the next day closing price for the S&P 500
"""

import pandas as pd
import numpy as np
from datetime import datetime
import sys
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# *** BEGIN FUNCTIONS ***
def calculate_closing_trends(df, new_column_name, trading_days, func):
    """
    :param df: Sorted data frame
    :param new_column_name: A new column that will house the average of N previous closing rows
    :param trading_days: number of days (N) to calculate the average for
    :param func: the function applied on rows. for example, 'avg', 'std'
    :return: a data frame with the average closing prices
    """
    df[new_column_name] = 0
    counter = 0
    temp_lst = []
    for index, row in df.iterrows():
        if counter < trading_days:
            temp_lst.append(row["Close"])
        if counter >= trading_days:
            if func == "avg":
                df.ix[index, new_column_name] = np.mean(temp_lst)
            elif func == "std":
                df.ix[index, new_column_name] = np.std(temp_lst)
            temp_lst = []
            counter = -1
        counter += 1
    return df

def split_data_frame_by_date(df, year, month, day, operator):
    """
    :param df: the data frame to be split
    :param year: year
    :param month: month
    :param day: day
    :param operator: the date operator to split the data by
    :return: a subset of the original data frame
    """
    if operator == "<":
        return df[df["Date"] < datetime(year=year, month=month, day=day)]
    elif operator == ">=":
        return df[df["Date"] >= datetime(year=year, month=month, day=day)]

# *** END FUNCTIONS ***


def main():
    sp500_df = pd.read_csv("./data/sphist.csv")
    #convert Date column to date type
    sp500_df["Date"] = pd.to_datetime(sp500_df["Date"])
    sp500_df.sort_values(["Date"], ascending=True, inplace=True)

    #create new colunmns. these column are used to house the avg, std closing price for the last n days
    sp500_df = calculate_closing_trends(sp500_df, "prev_5_days_closing_avg", 5, "avg")
    sp500_df = calculate_closing_trends(sp500_df, "prev_30_days_closing_avg", 30, "avg")
    sp500_df = calculate_closing_trends(sp500_df, "prev_365_days_closing_avg", 365, "avg")
    sp500_df = calculate_closing_trends(sp500_df, "prev_5_days_closing_std", 5, "std")
    sp500_df = calculate_closing_trends(sp500_df, "prev_30_days_closing_std", 30, "std")
    sp500_df = calculate_closing_trends(sp500_df, "prev_365_days_closing_std", 365, "std")

    #bring only rows that have completed 365 days of data for the year
    sp500_df = sp500_df[sp500_df["Date"] > datetime(year=1951, month=1, day=2)]

    #drop row with NaN values
    sp500_df.dropna(axis=0)

    #plot all new columns against "Close"
    fig = plt.figure(figsize=(10,20))
    ax1 = fig.add_subplot(6,1,1)
    ax2 = fig.add_subplot(6,1,2)
    ax3 = fig.add_subplot(6,1,3)

    ax4 = fig.add_subplot(6,1,4)
    ax5 = fig.add_subplot(6,1,5)
    ax6 = fig.add_subplot(6,1,6)


    ax1.scatter(sp500_df["prev_5_days_closing_avg"],sp500_df["Close"])
    ax1.set_xlabel("prev_5_days_closing_avg")
    ax1.set_ylabel("Close")
    ax2.scatter(sp500_df["prev_30_days_closing_avg"],sp500_df["Close"])
    ax2.set_xlabel("prev_30_days_closing_avg")
    ax2.set_ylabel("Close")
    ax3.scatter(sp500_df["prev_365_days_closing_avg"],sp500_df["Close"])
    ax3.set_xlabel("prev_365_days_closing_avg")
    ax3.set_ylabel("Close")
    ax4.scatter(sp500_df["prev_5_days_closing_std"],sp500_df["Close"])
    ax4.set_xlabel("prev_5_days_closing_std")
    ax4.set_ylabel("Close")
    ax5.scatter(sp500_df["prev_30_days_closing_std"],sp500_df["Close"])
    ax5.set_xlabel("prev_30_days_closing_std")
    ax5.set_ylabel("Close")
    ax6.scatter(sp500_df["prev_365_days_closing_std"],sp500_df["Close"])
    ax6.set_xlabel("prev_365_days_closing_std")
    ax6.set_ylabel("Close")

    plt.show()


    #split data by date into train and test data frames
    train = split_data_frame_by_date(sp500_df, year=2013, month=1, day=1, operator="<")
    test = split_data_frame_by_date(sp500_df, year=2013, month=1, day=1, operator=">=")

    #init a linear regression model
    model = LinearRegression()
    features = ['prev_5_days_closing_avg', 'prev_30_days_closing_avg', 'prev_365_days_closing_avg', 'prev_5_days_closing_std', 'prev_30_days_closing_std', 'prev_365_days_closing_std']
    target = "Close"
    model.fit(train[features], train[target])
    predictions = model.predict(test[features])

    #calculate the Mean Absolute Error (MAE) and model score
    mae = sum(abs(predictions - test[target].tolist())) / len(predictions)
    print("Mean Absolute Error (MAE): {0}".format(mae))
    print("Model Score: {0}").format(model.score(train[features], train[target]))

    #create a file with predictions next to actual. Just interested!
    predictions = model.predict(sp500_df[features])
    predictions_series = pd.Series(predictions)
    sp500_df["predictions"] = predictions_series.values
    sp500_df.to_csv("./data/sphist_with_predictions.csv")

if __name__ == "__main__":
    sys.exit(0 if main() else 1)





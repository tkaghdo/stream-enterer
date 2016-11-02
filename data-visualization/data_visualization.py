__author__ = 'Tamby Kaghdo'

import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import seaborn as sns

#this function by dataquest.io
def is_profitable(row):
        if row["Profitability"] <= 1.0:
            return False
        return True

def main():
    hollywood_movies = pd.read_csv("../data/hollywood_movies.csv")
    print(hollywood_movies.head(5))
    print(hollywood_movies["exclude"].value_counts(dropna=False))
    #drop the exclude column because its all NaN
    hollywood_movies = hollywood_movies.drop("exclude",axis=1)
    print(hollywood_movies.head(5))

    fig = plt.figure(figsize=(6,10))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    ax1.scatter(hollywood_movies["Profitability"],hollywood_movies["Audience Rating"])
    ax1.set_xlabel("Profitability")
    ax1.set_ylabel("Audience Rating")
    ax2.scatter(hollywood_movies["Audience Rating"],hollywood_movies["Profitability"])
    ax2.set_ylabel("Profitability")
    ax2.set_xlabel("Audience Rating")
    ax1.set_title("Hollywood Movies, 2007-2011")
    ax2.set_title("Hollywood Movies, 2007-2011")
    #plt.show()

    normal_movies = hollywood_movies[hollywood_movies["Film"] != "Paranormal Activity"]
    scatter_matrix(normal_movies[["Profitability", "Audience Rating"]],figsize=(6, 6))
    #plt.show()

    normal_movies[['Critic Rating', 'Audience Rating']].boxplot()
    #plt.show()

    fig2 = plt.figure(figsize=(8,4))
    ax1 = fig2.add_subplot(1,2,1)
    ax2 = fig2.add_subplot(1,2,2)
    normal_movies = normal_movies.sort_values(["Year"])
    sns.boxplot(data=normal_movies, x="Year", y="Critic Rating", ax=ax1)
    sns.boxplot(data=normal_movies, x="Year", y="Audience Rating", ax=ax2)
    #plt.show()

    normal_movies["Profitable"] = normal_movies.apply(is_profitable, axis=1)
    print(normal_movies["Profitable"].value_counts())
    fig3 = plt.figure(figsize=(12,6))
    ax1 = fig3.add_subplot(1,2,1)
    ax2 = fig3.add_subplot(1,2,2)
    sns.boxplot(data=normal_movies,x="Profitable",y="Audience Rating", ax=ax1)
    sns.boxplot(data=normal_movies,x="Profitable",y="Critic Rating", ax=ax2)
    plt.show()


if __name__ == '__main__':
    main()
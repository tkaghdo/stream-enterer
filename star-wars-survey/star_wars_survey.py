__author__ = 'Tamby Kaghdo'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

star_wars = pd.read_csv("../data/star_wars.csv", encoding="ISO-8859-1")
print(star_wars.head(5))

#remove NaN
star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]

print(star_wars.head(5))

yes_no = {
    "Yes": True,
    "No": False
}

questions_1 = ["Have you seen any of the 6 films in the Star Wars franchise?","Do you consider yourself to be a fan of the Star Wars film franchise?"]
for i in questions_1:
    star_wars[i] = star_wars[i].map(yes_no)

print(star_wars.head(5))

movie_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for i in star_wars.columns[3:9]:
    star_wars[i] = star_wars[i].map(movie_mapping)

star_wars = star_wars.rename(columns={
        "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1",
        "Unnamed: 10": "ranking_2",
        "Unnamed: 11": "ranking_3",
        "Unnamed: 12": "ranking_4",
        "Unnamed: 13": "ranking_5",
        "Unnamed: 14": "ranking_6"
        })

print(star_wars.head(5))

star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)

#star_wars[star_wars.columns[9:15]].mean()
#bar chart for best movies
plt.bar(range(6), star_wars[star_wars.columns[9:15]].mean())
plt.show()

#add seen column
plt.bar(range(6), star_wars[star_wars.columns[3:9]].sum())
plt.show()

#break up by gender
males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]

plt.bar(range(6), males[males.columns[9:15]].mean())
plt.show()

plt.bar(range(6), females[females.columns[9:15]].mean())
plt.show()

plt.bar(range(6), males[males.columns[3:9]].sum())
plt.show()

plt.bar(range(6), females[females.columns[3:9]].sum())
plt.show()
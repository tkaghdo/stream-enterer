## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars["origin"].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
print(cars.head())
dummy_years = pd.get_dummies(cars["year"],prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)
cars = cars.drop("year", axis=1)
cars = cars.drop("cylinders", axis=1)
print(cars.head(5))

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]
multiplier = 0.7 * len(cars)
train = shuffled_cars.iloc[0:int(multiplier)]
test = shuffled_cars.iloc[int(multiplier):len(shuffled_cars)]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()
features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]
models = {}
for origin in unique_origins:
    model = LogisticRegression()
    x_train = train[features]
    y_train = train["origin"] == origin
    model.fit(x_train,y_train)
    models[origin] = model

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
for origin in unique_origins:
    X_test = test[features]
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)
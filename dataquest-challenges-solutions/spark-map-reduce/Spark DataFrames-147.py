## 1. Spark DataFrame ##


f = open('census_2010.json')

for i in range(0,4):
    print(f.readline())

## 2. Reading in data ##

# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))


## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
df.printSchema()

## 4. Pandas vs Spark DataFrames ##


df.show(5)

## 5. Row object ##


first_five = df.head(5)
for r in first_five:
    print(r.age)

## 6. Selecting columns ##

df[['age']].show()
df[['age', 'males', 'females']].show()

## 7. Filtering rows ##


fifty_plus = df[df['age'] > 5]
fifty_plus.show()

## 8. Comparing columns ##


df[df['females'] < df['males']].show()

## 9. Spark to Pandas ##


pandas_df = df.toPandas()
pandas_df['total'].hist()
## 1. Counting in Python ##


import sqlite3

conn = sqlite3.connect("factbook.db")
facts = conn.execute("select * from facts;").fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
birth_rate_count = conn.execute("select count(birth_rate) from facts;").fetchall()[0][0]
print(birth_rate_count)

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
min_population_growth = conn.execute("select min(population_growth ) from facts;").fetchall()[0][0]
print(min_population_growth)
max_death_rate = conn.execute("select max(death_rate ) from facts;").fetchall()[0][0]
print(max_death_rate)

## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
total_land_area = conn.execute("select sum(area_land) from facts;").fetchall()[0][0]
print(total_land_area)
avg_water_area = conn.execute("select avg(area_water) from facts;").fetchall()[0][0]
print(avg_water_area)

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
q = "select avg(population), sum(population),max(birth_rate) from facts;"
facts_stats = conn.execute(q).fetchall()
print(facts_stats)

## 6. Conditional aggregation ##

conn = sqlite3.connect("factbook.db")
q = "select avg(population_growth) from facts where population > 10000000;"
population_growth = conn.execute(q).fetchall()[0][0]
print(population_growth)

## 7. Selecting unique rows ##

conn = sqlite3.connect("factbook.db")
q = "select distinct birth_rate from facts"
unique_birth_rates = conn.execute(q).fetchall()
print(unique_birth_rates)

## 8. Distinct aggregations ##

conn = sqlite3.connect("factbook.db")
q1 = "select avg(distinct birth_rate ) from facts where population  > 20000000"
average_birth_rate = conn.execute(q1).fetchall()[0][0]
print(average_birth_rate)
q2 = "select sum(distinct population) from facts where area_land > 1000000"
sum_population = conn.execute(q2).fetchall()[0][0]
print(sum_population)

## 9. Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
q = "select population_growth / 1000000.0 from facts"
population_growth_millions = conn.execute(q).fetchall()
print(population_growth_millions)

## 10. Arithmetic between columns ##

conn = sqlite3.connect("factbook.db")
q = "select (population * population_growth ) + population from facts"
next_year_population = conn.execute(q).fetchall()
print(next_year_population)
## 3. Connect to the database ##

import sqlite3
conn = sqlite3.connect("jobs.db")

## 6. Running a query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])
q = "select Major from recent_grads;"
cursor.execute(q);
majors = cursor.fetchall()
print(majors[0:2])

## 8. Fetching a specific number of results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
q = "select Major, Major_category from recent_grads;"
five_results = conn.execute(q).fetchmany(5)

## 9. Closing the connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

conn = sqlite3.connect("jobs2.db")
q = "select Major from recent_grads order by 1 desc;"
reverse_alphabetical = conn.execute(q).fetchall()
conn.close()
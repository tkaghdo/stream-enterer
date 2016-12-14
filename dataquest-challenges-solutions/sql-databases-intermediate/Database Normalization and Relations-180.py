## 4. Querying a normalized database ##

q = "select ceremonies.year, nominations.movie from ceremonies inner join nominations on ceremonies.id == nominations.ceremony_id where nominations.nominee = 'Natalie Portman'"
portman_movies = conn.execute(q).fetchall()
print(portman_movies)


## 6. Join table ##

q1 = "select * from movies_actors limit 5;"
q2 = "select * from actors limit 5;"
q3 = "select * from movies limit 5;"
five_join_table = conn.execute(q1).fetchall()
five_actors = conn.execute(q2).fetchall()
five_movies = conn.execute(q3).fetchall()
print(five_join_table)
print(five_actors)
print(five_movies)


## 7. Querying a many-to-many relation ##

q = '''SELECT actors.actor, movies.movie FROM movies INNER JOIN movies_actors ON movies.id == movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id == actors.id WHERE movies.movie == "The King's Speech"''';
kings_actors = conn.execute(q).fetchall()
print(kings_actors)

## 8. Practice: querying a many-to-many relation ##

q = '''select movies.movie, actors.actor from movies inner join movies_actors on  movies_actors.movie_id == movies.id inner join actors on movies_actors.actor_id == actors.id where actors.actor == "Natalie Portman"'''
portman_joins = conn.execute(q).fetchall()
print(portman_joins)
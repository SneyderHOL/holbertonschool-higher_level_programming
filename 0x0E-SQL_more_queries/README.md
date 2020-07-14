# Project 0x0E SQL - More queries

Project using SQL, containing severall scripts with sql.

Concepts:

    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What’s a PRIMARY KEY
    What’s a FOREIGN KEY
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What are subqueries
    What are JOIN and UNION


Decribing each script:

0-privileges.sql is a script that list all privilages of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

1-create_user.sql is a script that creates the MySQL server user user_od_1.

2-create_read_user.sql is a script that creates the database hbtn_0d_2 and the user user_0d_2.

3-force_name.sql is a script that creates the table force_name on your MySQL server.

4-never_empty.sql is a script that creates the table id_not_null on your MySQL server.

5-unique_id.sql is a script that creates the table unique_id on your MySQL server.

6-states.sql is a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

7-cities.sql is a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

8-cities_of_california_subquery.sql is a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

9-cities_by_state_join.sql is a script that lists all cities contained in the database hbtn_0d_usa.

10-genre_id_by_show.sql is a script that list all shows contained in hbtn_0d_tvshows that have at least one genre linked.

11-genre_id_all_shows.sql is a script that list all shows contained hbtn_0d_tvshows.

12-no_genre.sql is a script that list all shows contained in hbtn_0d_tvshows without a genre linked.

13-count_shows_by_genre.sql is a script that list all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

14-my_genres.sql is a script that uses the hbtn_0d_tvshows database to list all genres of the show Dexter.

15-comedy_only.sql is a script that list all Comedy shows in the database hbtn_0d_tvshows_.

16-shows_by_genre.sql is a script that list all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

100-not_my_genres.sql is a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.

101-not_a_comedy.sql is a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

102-rating_shows.sql is a script that list all shows from hbtn_0d_tvshows_rate by their rating.

103-rating_genres.sql is a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

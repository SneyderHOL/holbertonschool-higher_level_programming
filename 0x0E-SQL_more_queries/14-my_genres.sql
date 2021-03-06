-- list all genres of the show Dexter from hbtn_0d_tvshows.
SELECT tv_genres.name
FROM tv_shows
     INNER JOIN tv_show_genres
     ON tv_shows.id = tv_show_genres.show_id
     INNER JOIN tv_genres
     ON tv_genres.id = tv_show_genres.genre_id
WHERE title = 'Dexter'
ORDER BY tv_genres.name;

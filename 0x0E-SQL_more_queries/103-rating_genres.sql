SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
FROM tv_genres
INNER JOIN tv_shows
ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.id
ORDER BY rating_sum DESC;

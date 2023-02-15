SELECT tv_genres.name, SUM(rating) as rating_sum
FROM tv_genres
JOIN tv_shows
ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;

SELECT title
FROM tv_shows
WHERE genre_id NOT IN (SELECT id FROM tv_genres WHERE name = 'Comedy')
ORDER BY title ASC;

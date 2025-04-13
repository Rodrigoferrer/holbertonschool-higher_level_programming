SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM genres g
JOIN tv_shows s ON g.id = s.genre_id
GROUP BY g.id
HAVING COUNT(s.id) > 0
ORDER BY number_of_shows DESC;
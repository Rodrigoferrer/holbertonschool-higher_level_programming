SELECT g.name
FROM tv_shows s
JOIN tv_genres g ON s.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
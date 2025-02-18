SELECT 
	c.photo_id,
	p.capture_date,
	p.description,
	COUNT(c.id) AS comments_count
FROM
	comments AS c
LEFT JOIN
	photos AS p
	ON p.id = c.photo_id
WHERE 
	p.description IS NOT NULL
GROUP BY
	c.photo_id,
	p.capture_date,
	p.description
ORDER BY
	COUNT(c.id) DESC,
	c.photo_id 
LIMIT 
	3

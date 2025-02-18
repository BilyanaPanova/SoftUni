SELECT 
	o.name AS owner,
	COUNT(a.id) AS count_of_animals
FROM
	animals AS a
JOIN 
	owners AS o
	ON o.id = a.owner_id
GROUP BY
	o.name
ORDER BY 
	COUNT(a.id) DESC,
	o.name
LIMIT 
	5;

SELECT 
	bg.id,
	bg.name,
	bg.release_year,
	c.name AS category_name
FROM 
	board_games AS bg
JOIN 
	categories AS c
	ON bg.category_id = c.id
WHERE 
	c.name IN ('Strategy Games','Wargames')
ORDER BY 
	bg.release_year DESC

SELECT 
	c.id,
	CONCAT(c.first_name,' ',c.last_name) AS creator_name,
	c.email
FROM 
	creators_board_games AS cbg
RIGHT JOIN 
	creators AS c 
	ON cbg.creator_id = c.id
WHERE 
	cbg.creator_id IS NULL

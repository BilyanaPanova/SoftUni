SELECT 
	c.last_name,
	CEIL(AVG(bg.rating)) AS average_rating,
	p.name
FROM 
	board_games AS bg
JOIN 
	creators_board_games as cbg
	ON bg.id = cbg.board_game_id
JOIN 
	creators AS c
	ON cbg.creator_id = c.id
JOIN 
	publishers AS p
	ON bg.publisher_id = p.id
WHERE 
	p.name = 'Stonemaier Games'
GROUP BY 
	c.last_name,
	p.name
ORDER BY
	average_rating DESC

UPDATE coaches
SET salary = salary * coach_level
WHERE first_name LIKE 'C%' 
	AND 
	id in (SELECT coach_id FROM players_coaches);

SELECT * FROM players_coaches

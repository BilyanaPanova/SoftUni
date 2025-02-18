INSERT INTO coaches(first_name,last_name,salary,coach_level)
SELECT 
	first_name,
	last_name,
	salary * 2 AS salary,
	char_length(first_name)
FROM 
	players
WHERE 
	hire_date < '2013-12-13 07:18:46'

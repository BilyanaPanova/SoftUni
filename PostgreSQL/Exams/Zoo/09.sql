SELECT 
	name AS volunteers,
	phone_number,
	SUBSTRING(address FROM '[0-9].*') AS address
FROM 
	volunteers 
WHERE 
	address LIKE '%Sofia%'
	AND 
	department_id = (
					SELECT id
					FROM volunteers_departments
					WHERE department_name = 'Education program assistant'
					)
ORDER BY
	name

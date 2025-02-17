SELECT 
	a.name AS animal,
	EXTRACT(year from a.birthdate) AS birth_year,
	at.animal_type
FROM 
	animals AS a
JOIN 
	animal_types AS at
	ON a.animal_type_id = at.id
WHERE 
	a.owner_id IS NULL
	AND 
	(2022 - 5) <= EXTRACT(year from a.birthdate)
	AND 
	at.animal_type != 'Birds'
ORDER BY
	a.name

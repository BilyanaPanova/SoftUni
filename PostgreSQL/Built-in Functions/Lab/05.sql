SELECT
	first_name,
	last_name,
	date_part('year', born) AS year
FROM authors
ORDER BY id;

--OR 

SELECT
	first_name,
	last_name,
	EXTRACT(year FROM born) AS year
FROM authors
ORDER BY id;

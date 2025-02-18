SELECT
	population,
	LENGTH(population::text) AS "length"
FROM countries;

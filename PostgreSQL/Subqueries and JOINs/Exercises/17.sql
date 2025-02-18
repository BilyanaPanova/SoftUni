UPDATE 
	countries
SET 
	country_name = 'Burma'
WHERE 
	country_name = 'Myanmar';

INSERT INTO 
	monasteries(monastery_name,country_code)
VALUES
	('Hanga Abbey', 
		(SELECT country_code 
			FROM countries 
			WHERE country_name = 'Tanzania')),
	('Myin-Tin-Daik', 
		(SELECT country_code 
			FROM countries 
			WHERE country_name = 'Myanmar'));

SELECT 
	c.continent_name,
	cou.country_name,
	COUNT(m.id) AS "monasteries_count"
FROM continents AS c
LEFT JOIN countries AS cou
	ON c.continent_code = cou.continent_code
LEFT JOIN monasteries AS m
	ON m.country_code = cou.country_code
WHERE 
	NOT cou.three_rivers
GROUP BY 
	country_name,
	continent_name
ORDER BY 
	"monasteries_count" DESC,
	country_name;

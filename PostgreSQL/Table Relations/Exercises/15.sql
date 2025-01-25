SELECT 
	COUNT(*) AS countries_without_rivers
FROM 
	countries c
LEFT JOIN 
	countries_rivers cr 
ON 
	cr.country_code = c.country_code
WHERE 
	cr.country_code IS NULL;

CREATE VIEW view_continents_countries_currencies_details AS
SELECT 
	concat(c2.continent_name,': ',c2.continent_code) AS continent_details,
	FORMAT('%s - %s - %s - km2',c1.country_name,c1.capital,c1.area_in_sq_km) AS country_information,
	concat(c3.description,' (',c3.currency_code,')') AS currencies
FROM countries c1
         JOIN continents c2 ON c1.continent_code = c2.continent_code
         JOIN currencies c3 ON c3.currency_code = c1.currency_code
ORDER BY 
	country_information,
	currencies;

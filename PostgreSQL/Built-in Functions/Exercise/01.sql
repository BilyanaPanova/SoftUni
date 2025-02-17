CREATE VIEW view_river_info AS
SELECT 
	FORMAT ('The river %s flows into the %s and is %s kilometers long.',river_name,outflow,length) 
	AS "River Information"
FROM rivers
ORDER BY river_name;

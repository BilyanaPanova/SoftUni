CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
DECLARE 
	e_count INT;
BEGIN 
	SELECT 
		COUNT(*) INTO e_count
	FROM employees AS e
	JOIN 
		addresses AS a
		ON e.address_id = a.address_id
	JOIN 
		towns AS t
		ON a.town_id = t.town_id
	WHERE t.name = town_name;
	RETURN e_count;
END;
$$
LANGUAGE plpgsql;

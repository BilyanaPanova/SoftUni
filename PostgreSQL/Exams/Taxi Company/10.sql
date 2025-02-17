CREATE OR REPLACE FUNCTION fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS $$
	DECLARE 
		count_courses INT ;
	BEGIN 
		SELECT 
			COUNT(co.id)
		FROM 
			clients AS cl
		JOIN courses AS co
			ON cl.id = co.client_id
		WHERE cl.phone_number = phone_num
		GROUP BY
			cl.id
		INTO count_courses;
		RETURN COALESCE(count_courses,0);
	END;
$$
LANGUAGE plpgsql;

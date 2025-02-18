CREATE OR REPLACE PROCEDURE sp_customer_country_name(
	IN customer_full_name VARCHAR(50) ,
	OUT country_name VARCHAR(50)
	) 
LANGUAGE plpgsql
AS $$
	BEGIN
		SELECT 
			name INTO country_name
		FROM
			countries
		WHERE id = (
					SELECT country_id
					FROM customers 
					WHERE CONCAT(first_name,' ',last_name) = customer_full_name
		);
	END;
$$

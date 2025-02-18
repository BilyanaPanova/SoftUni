CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(IN product_name VARCHAR(25))
RETURNS TABLE (customer_id INT,
				customer_name VARCHAR(75),
				feedback_description varchar(255),
				feedback_rate NUMERIC(4,2)
				)
AS $$
	BEGIN 
		RETURN QUERY
			SELECT
				c.id,
				c.first_name,
				f.description,
				f.rate
			FROM
				customers AS c 
			JOIN 
				feedbacks AS f
				ON c.id= f.customer_id
			WHERE 
				f.product_id IN (select id from products where name = product_name)
			ORDER bY c.id;
	END;
$$
LANGUAGE plpgsql;

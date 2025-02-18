CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE (
				total_cash NUMERIC
			   )
AS $$
	BEGIN
		RETURN QUERY
	    SELECT ROUND(SUM(cash), 2) AS total_cash
	    FROM (
	        SELECT 
				cash,
				ROW_NUMBER() OVER (ORDER BY cash DESC) AS row_num
			FROM users_games AS ug 
			JOIN games AS g 
				ON ug.game_id = g.id 
			WHERE g.name = game_name
			ORDER BY ug.cash DESC
	    ) AS ranked_rows
	    WHERE row_num % 2 = 1;  
	END;
$$
 LANGUAGE plpgsql;

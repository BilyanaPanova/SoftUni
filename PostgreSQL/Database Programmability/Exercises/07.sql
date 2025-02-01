CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
LANGUAGE plpgsql
AS $$
	DECLARE
	holder_info RECORD;
	BEGIN 
		FOR holder_info IN
			SELECT
				CONCAT(ah.first_name,' ',ah.last_name) AS "holder",
				SUM(a.balance) AS total_balance
			FROM 
				accounts AS a
			LEFT JOIN 
				account_holders AS ah
				ON a.account_holder_id = ah.id
			GROUP BY 
				"holder"
			HAVING 
				SUM(a.balance) > searched_balance
			ORDER BY 
				"holder"
		LOOP
			RAISE NOTICE '% - %', holder_info.holder,holder_info.total_balance;
		END LOOP;
	END;
$$;

CALL sp_retrieving_holders_with_balance_higher_than(200000)

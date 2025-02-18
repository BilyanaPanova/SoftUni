CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT,money_amount NUMERIC)
LANGUAGE plpgsql
AS $$
	BEGIN 
		IF EXISTS (SELECT 
                  *
                FROM 
                  accounts
                WHERE id = account_id AND balance >= money_amount
                ) THEN 
  			UPDATE 
  				accounts
  			SET balance = balance - money_amount
  			WHERE id = account_id;
  			COMMIT;
		ELSE
			ROLLBACK;
		END IF;
	END;
$$

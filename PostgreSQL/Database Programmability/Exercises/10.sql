CREATE OR REPLACE PROCEDURE sp_transfer_money(sender_id INT,receiver_id INT,amount NUMERIC)
LANGUAGE plpgsql
AS $$
	BEGIN 
		IF EXISTS (
					SELECT 
						*
					FROM 
						accounts
					WHERE 
						id in (sender_id,receiver_id)
					) AND 
					(SELECT 
						balance
					FROM 
						accounts
					WHERE 
						id = sender_id) > amount THEN 
			CALL sp_deposit_money(receiver_id,amount);
			CALL sp_withdraw_money(sender_id,amount);
		ELSE 
			ROLLBACK;
		END IF;
	END;
$$

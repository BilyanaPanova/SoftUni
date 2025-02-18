CREATE OR REPLACE FUNCTION fn_creator_with_board_games(IN first_name_in VARCHAR(30),OUT total_board_games INT)
AS $$
	BEGIN 
		SELECT 
			COUNT(board_game_id) as games
		FROM 
			creators as c
		JOIN 
			creators_board_games as cbg
			ON c.id = cbg.creator_id
		WHERE c.first_name = first_name_in
		
		INTO total_board_games;
	END;
$$
LANGUAGE plpgsql;


--OR

CREATE OR REPLACE FUNCTION fn_creator_with_board_games(first_name_in VARCHAR(30))
RETURNS INT
AS $$
	DECLARE total_board_games INT;
	BEGIN 
		SELECT 
			COUNT(board_game_id) INTO total_board_games
		FROM 
			creators as c
		JOIN 
			creators_board_games as cbg
			ON c.id = cbg.creator_id
		WHERE c.first_name = first_name_in;
		RETURN total_board_games;
	END;
$$
LANGUAGE plpgsql;

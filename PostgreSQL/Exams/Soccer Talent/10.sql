CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT COALESCE(t.name, 'The player currently has no team') 
    INTO team_name
    FROM players p
    LEFT JOIN teams t ON p.team_id = t.id
    WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;
END;
$$;


--OR

CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(100)
)
LANGUAGE plpgsql
AS $$
DECLARE 
    team_id_n INT;
BEGIN
    SELECT team_id INTO team_id_n
    FROM players
    WHERE CONCAT(first_name, ' ', last_name) = player_name;

    IF team_id_n IS NULL THEN
        team_name := 'The player currently has no team';
    ELSE
        SELECT name INTO team_name
        FROM teams
        WHERE id = team_id_n;
    END IF;
END;
$$;

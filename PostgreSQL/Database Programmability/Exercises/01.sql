CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS $$
DECLARE 
    full_name VARCHAR;
BEGIN 
    IF first_name IS NULL AND last_name IS NULL THEN
        RETURN NULL;
    ELSIF first_name IS NULL THEN
        RETURN INITCAP(last_name);
    ELSIF last_name IS NULL THEN
        RETURN INITCAP(first_name);
    ELSE
        RETURN CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
    END IF;
END;
$$ LANGUAGE plpgsql;

--OR

CREATE OR REPLACE FUNCTION fn_full_name(IN first_name VARCHAR, IN last_name VARCHAR,
										OUT full_name VARCHAR)
AS $$
BEGIN 
    IF first_name IS NOT NULL AND last_name IS NOT NULL THEN
        full_name := CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
    ELSIF first_name IS NOT NULL THEN
        full_name := INITCAP(first_name);
    ELSIF last_name IS NOT NULL THEN
        full_name := INITCAP(last_name);
    ELSE 
        full_name := NULL;
    END IF;
END;
$$ LANGUAGE plpgsql;

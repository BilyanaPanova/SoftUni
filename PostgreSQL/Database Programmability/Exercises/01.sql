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

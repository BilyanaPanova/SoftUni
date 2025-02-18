CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    											set_of_letters VARCHAR(50), 
   												word VARCHAR(50)
												) 
RETURNS BOOLEAN 
AS $$
	DECLARE
	    i INT;
	    letter CHAR;
	    letter_count INT;
	    set_letter_count INT;
	BEGIN
	    set_of_letters := LOWER(set_of_letters);
	    word := LOWER(word);
	    word := REGEXP_REPLACE(word, '[^a-z]', '', 'g');
	    FOR i IN 1..LENGTH(word) LOOP
	        letter := SUBSTRING(word FROM i FOR 1);
	        SELECT COUNT(*) INTO letter_count FROM regexp_split_to_table(word, '') AS x WHERE x = letter;
	        SELECT COUNT(*) INTO set_letter_count FROM regexp_split_to_table(set_of_letters, '') AS x WHERE x = letter;
	        IF letter_count > set_letter_count THEN
	            RETURN FALSE;
	        END IF;
	    END LOOP;
	
	    RETURN TRUE;
END;
$$ 
LANGUAGE plpgsql;

SELECT 
    (regexp_matches("River Information", '([0-9]{1,4})'))[1]::INTEGER AS river_length
FROM 
    view_river_info;

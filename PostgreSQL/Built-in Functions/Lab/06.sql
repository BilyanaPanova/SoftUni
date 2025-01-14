SELECT
	last_name "Last Name",
	to_char(born,'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors
ORDER BY id;

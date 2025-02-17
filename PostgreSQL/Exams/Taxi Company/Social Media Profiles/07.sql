SELECT
	CONCAT(a.id,' ',a.username) AS id_username,
	a.email
FROM
	accounts AS a
JOIN
	accounts_photos as ap
	ON a.id = ap.account_id
WHERE 
	ap.account_id = ap.photo_id
ORDER BY
	a.id


--OR


SELECT
	CONCAT(id, ' ', username) AS id_username,
	email
FROM 
	accounts
WHERE 
	id IN (
		SELECT account_id 
		FROM accounts_photos 
		WHERE account_id = photo_id
		)
ORDER BY 
	id;

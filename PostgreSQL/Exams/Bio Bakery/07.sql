SELECT 
	p.name AS product_name,
	ROUND(AVG(p.price),2) AS average_price,
	COUNT(f.id) AS total_feedbacks
FROM 
	products AS p
JOIN 
	feedbacks AS f
	ON f.product_id = p.id
WHERE 
	(p.price > 15)
GROUP BY
	p.name
HAVING
	COUNT(f.id) > 1
ORDER BY
	COUNT(f.id),
	ROUND(AVG(p.price),2) DESC

SELECT
	id,
	(t.side * t.height) / 2 AS area
FROM triangles AS t
ORDER BY id;

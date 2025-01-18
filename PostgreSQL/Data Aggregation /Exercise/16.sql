SELECT 
	project_name,
	CASE 
		WHEN start_date is NOT NULL AND end_date is NOT NULL THEN 'Done'
		WHEN start_date is NOT NULL AND end_date is NULL THEN 'In Progress'
		ELSE 'Ready for development'
	END AS project_status

FROM projects
WHERE project_name LIKE '%Mountain%';

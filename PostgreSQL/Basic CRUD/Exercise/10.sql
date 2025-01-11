SELECT 
	employee_id,
	project_id
FROM employees_projects
WHERE employee_id = 200 OR employee_id = 250 AND NOT (project_id IN (50,100))
;

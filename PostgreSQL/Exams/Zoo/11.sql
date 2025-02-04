CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
							IN searched_volunteers_department VARCHAR(30),
							OUT count_of_volunteers INT)
AS $$
	BEGIN
		SELECT 
			COALESCE(COUNT(*), 0)
      INTO count_of_volunteers
		FROM 
			volunteers
		WHERE 
			department_id = (SELECT id
							 FROM volunteers_departments
							 WHERE department_name = searched_volunteers_department);
	END;
$$
LANGUAGE plpgsql;

CREATE PROCEDURE sp_increase_salaries(department_name VARCHAR)
AS $$
	BEGIN 
		UPDATE employees AS e
		SET salary = salary * 1.05
		WHERE e.department_id = (
			SELECT 
				department_id
			FROM departments AS d
			WHERE d.name = department_name
		);
	END;
$$
LANGUAGE plpgsql;

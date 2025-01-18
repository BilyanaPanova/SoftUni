CREATE TABLE employees_projects (
    id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    CONSTRAINT fk_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_project
        FOREIGN KEY (project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE
);

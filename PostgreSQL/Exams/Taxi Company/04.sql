DELETE FROM clients
WHERE id NOT IN (SELECT client_id FROM courses);

--OR 

DELETE FROM clients
WHERE NOT EXISTS (
    SELECT 1 FROM courses WHERE courses.client_id = clients.id
);

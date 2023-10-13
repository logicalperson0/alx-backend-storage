-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $
CREATE PROCEDURE AddBonus (user_id INT, project_name varchar(255), score INT)
    BEGIN
        declare c INT default 0;
        declare pro INT default 0;

        SELECT COUNT(id)
        INTO c
        FROM projects
        WHERE name = project_name;

        IF c = 0 THEN
           INSERT INTO projects(name) VALUES (project_name);
        END IF;

        SELECT id
        INTO pro
        FROM projects
        WHERE name = project_name;

        INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, pro, score);
    END $
DELIMITER ;

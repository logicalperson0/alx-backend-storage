-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
    BEGIN
        DECLARE pro_cou INT default 0;
        DECLARE tot_sco INT DEFAULT 0;

        SELECT SUM(score)
        INTO tot_sco
        FROM corrections
        WHERE corrections.user_id = user_id;

        SELECT COUNT(*)
        INTO pro_cou
        FROM corrections
        WHERE corrections.user_id = user_id;

        UPDATE users
           SET users.average_score = tot_sco / pro_cou
           WHERE users.id = user_id;
    END $
DELIMITER ;

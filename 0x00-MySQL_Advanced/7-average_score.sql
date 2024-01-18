-- Script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score INT;
    DECLARE total_projects INT;

    -- Compute the total score and total number of projects for the user
    SELECT SUM(score), COUNT(DISTINCT project_id) INTO total_score, total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average score
    UPDATE users
    SET average_score = IF(total_projects > 0, total_score / total_projects, 0)
    WHERE id = user_id;
END;
//

DELIMITER ;


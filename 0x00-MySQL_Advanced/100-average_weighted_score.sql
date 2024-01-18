-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE total_score INT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;

    -- Calculate the total weighted score and weight
    SELECT SUM(score * weight) INTO total_score, SUM(weight) INTO total_weight
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the average_weighted_score in the users table
    UPDATE users
    SET average_weighted_score = IF(total_weight > 0, total_score / total_weight, 0)
    WHERE id = p_user_id;
END //

DELIMITER ;


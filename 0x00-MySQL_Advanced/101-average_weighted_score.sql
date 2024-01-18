-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;
    
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE user_id INT;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN user_cursor;
    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        DECLARE total_score INT DEFAULT 0;
        DECLARE total_weight INT DEFAULT 0;

        -- Calculate the total weighted score and weight
        SELECT SUM(score * weight) INTO total_score, SUM(weight) INTO total_weight
        FROM corrections
        WHERE user_id = user_id;

        -- Update the average_weighted_score in the users table
        UPDATE users
        SET average_weighted_score = IF(total_weight > 0, total_score / total_weight, 0)
        WHERE id = user_id;
    END LOOP;

    CLOSE user_cursor;
END //

DELIMITER ;


-- Script that creates an index idx_name_first_score
DELIMITER //

-- Create the SafeDiv function
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 5)
BEGIN
    DECLARE result DECIMAL(10, 5);

    -- Check if b is not equal to 0
    IF b != 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;

    RETURN result;
END //

DELIMITER ;


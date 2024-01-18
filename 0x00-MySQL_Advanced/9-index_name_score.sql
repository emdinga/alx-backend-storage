-- Ensure the names table exists
CREATE TABLE IF NOT EXISTS names (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);

-- Create the index on the first letter of the name and the score
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);


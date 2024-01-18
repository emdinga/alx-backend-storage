-- Script that creates an index idx_name_first
-- ensure the script exist
CREATE TABLE IF NOT EXISTS names (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);\

-- Create the index on the first letter of the name
CREATE INDEX idx_name_first ON names (LEFT(name, 1));

-- Task: Create the unique_id table

-- Create the table if it does not already exist.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

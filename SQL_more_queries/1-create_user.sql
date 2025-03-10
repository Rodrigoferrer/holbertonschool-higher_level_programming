
-- Create a user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
-- a SQL script that creates a table users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    email varchar(255),
    name varchar(255),
    PRIMARY KEY (id)
);

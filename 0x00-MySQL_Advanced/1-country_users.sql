-- a SQL script that creates a table users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country varchar(2) NOT NULL DEFAULT 'US' CHECK(country IN ('US', 'CO', 'IN')),
    PRIMARY KEY (id)
);

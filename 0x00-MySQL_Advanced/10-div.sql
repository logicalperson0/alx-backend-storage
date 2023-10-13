-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
DELIMITER $
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT deterministic
BEGIN
    declare divs FLOAT default 0;
    IF b != 0 THEN
       SET divs = a / b;
       RETURN divs;
    END IF;
    RETURN divs;
END $
DELIMITER ;

USE db;

CREATE TABLE IF NOT EXISTS studio (
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL
);

DELIMITER //
CREATE PROCEDURE insert_pacet_of_studious()
BEGIN
	DECLARE counter INT DEFAULT 1;
	WHILE counter <= 10 DO
		INSERT INTO studio (name) VALUES (CONCAT('Noname', counter));
        SET counter = counter  + 1; 
    END WHILE;
END //

DELIMITER ;

CALL insert_pacet_of_studious();

-- Тригер для вставки (оновлення) фільму
DELIMITER //
CREATE  TRIGGER before_insert_film
-- CREATE TRIGGER before_update_film
BEFORE INSERT 
-- BEFORE UPDATE 
ON film
FOR EACH ROW
BEGIN
    DECLARE studio_count INT;

   SELECT COUNT(*) INTO studio_count FROM studio WHERE id = NEW.studio_id;

    IF studio_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'There is no studio with this id';
    END IF;
END;
//
DELIMITER ;


-- Тригер для видалення студії
DELIMITER //
CREATE TRIGGER before_delete_studio
BEFORE DELETE 
ON studio
FOR EACH ROW
BEGIN
    DECLARE film_count INT;

    SELECT COUNT(*) INTO film_count FROM film WHERE studio_id = OLD.id;

    IF film_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Unable to delete studio because there are related movies.';
    END IF;
END;
//
DELIMITER ;


--  Тригер для заборони зміни даних в таблиці
DELIMITER //
CREATE TRIGGER forbid_update_film_top_cast
BEFORE UPDATE 
ON film_top_cast 
FOR EACH ROW 
BEGIN 
	SIGNAL SQLSTATE '45000'
	SET MESSAGE_TEXT = 'Forbidden action: Not allowed to udate';	
END //
DELIMITER ;

-- Тригер для обмеження дозволених імен для юзера 
DELIMITER //
CREATE TRIGGER alowed_insert_user_names
BEFORE INSERT 
ON `user` 
FOR EACH ROW 
BEGIN 
	IF NEW.first_name  NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN 
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Unacceptable user name';
	END IF;
END;
//
DELIMITER ;


--  Тригер для збереження логів зі зміною review
CREATE TABLE log_review (
  id INT NOT NULL AUTO_INCREMENT,
  review_id INT NOT NULL, 
  `date` DATETIME NOT NULL,
  user_id INT NOT NULL,
  film_id INT NOT NULL,
  `comment` TINYTEXT DEFAULT NULL,
  mark TINYINT DEFAULT NULL,
  PRIMARY KEY (id, review_id)
);

DELIMITER //
CREATE TRIGGER log_reviews_on_update
AFTER UPDATE 
ON review 
FOR EACH ROW 
BEGIN 
	INSERT INTO log_review (review_id, `date`, user_id, film_id, comment, mark ) VALUES 
	(OLD.id, CURRENT_TIMESTAMP, OLD.user_id, OLD.film_id, OLD.comment, OLD.mark);
END //
DELIMITER ;

-- Процедура для вставлення нового жанру
DELIMITER //
CREATE PROCEDURE insert_genre(IN genre_name VARCHAR(45))
BEGIN
    INSERT INTO genre (`name`) VALUES (genre_name);
END //

DELIMITER ;

-- Процедура для створення звязку m:m
DELIMITER //
CREATE PROCEDURE insert_film_genre(
	IN film_id INT,
	IN genre_id INT
)
BEGIN
	DECLARE film_count INT;
    DECLARE genre_count INT;
	
    SELECT COUNT(*) INTO film_count FROM film WHERE film.id = film_id;
    SELECT COUNT(*) INTO genre_count FROM genre WHERE genre.id = genre_id;
	
	IF film_count = 0 OR genre_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'There is no movie or genre with this id';
    END IF;
	
	INSERT INTO film_genre (film_id, genre_id) VALUES (film_id, genre_id);
END //

DELIMITER ;

-- Функція, яка повретає max, min, avg значення для стовпця film.point
DELIMITER //
CREATE FUNCTION get_films_point(aggregate_type VARCHAR(3))
RETURNS DECIMAL(2,1)
deterministic
BEGIN
	DECLARE result DECIMAL(2, 1);
    
    IF aggregate_type = 'max' THEN
        SELECT MAX(point) INTO result FROM film;
    ELSEIF aggregate_type = 'min' THEN
        SELECT MIN(point) INTO result FROM film;
    ELSEIF aggregate_type = 'avg' THEN
        SELECT AVG(point) INTO result FROM film;
    ELSE
		SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'There is no method for this';
    END IF;

    RETURN result;
END //

DELIMITER //

CREATE PROCEDURE get_films_point_statistics(IN aggregate_type VARCHAR(3))
BEGIN
	SELECT get_films_point(aggregate_type) as point;
END //
DELIMITER ; 

-- Створення таблиць за назвами країн

DROP PROCEDURE IF EXISTS create_tables_from_country;

DELIMITER //
CREATE PROCEDURE create_tables_from_country()
BEGIN
	DECLARE done int DEFAULT false;
	DECLARE country_name varchar(45);
    
    DECLARE Country_Cursor CURSOR
		FOR SELECT name FROM country;
	
	DECLARE CONTINUE HANDLER
		FOR NOT FOUND SET done = true;
	
    OPEN Country_Cursor;
    
    createTable: LOOP
		FETCH Country_Cursor INTO country_name;
        IF done=true THEN LEAVE createTable;
        END IF;
        SET @temp_query=CONCAT(
			"CREATE TABLE ",
            country_name,
            "_",
            REPLACE(CURRENT_DATE(), "-", "_"),
			" (
				id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
				`name` VARCHAR(45) NOT NULL
			);
			"
        );
        PREPARE SQLString FROM @temp_query;
        EXECUTE SQLString;
        DEALLOCATE PREPARE SQLString;
        END LOOP;
        
	CLOSE Country_Cursor;
END //
DELIMITER ;


CALL create_tables_from_country();
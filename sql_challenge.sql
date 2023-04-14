CREATE DATABASE foundation_assessment_ii;
USE foundation_assessment_ii;


CREATE TABLE movie_info (
    movie_ID int NOT NULL,
    movie_name varchar(255),
    movie_length time,
    age_rating varchar(3),
    Primary Key(movie_ID)
);

CREATE TABLE screens (
    screen_ID int NOT NULL,
    four_K varchar(6),
    Primary Key(screen_ID)
);

CREATE TABLE showings (
    showing_ID int NOT NULL,
    movie_ID int NOT NULL,
	screen_ID int NOT NULL,
    start_time time, 
    available_seats int,
    Primary Key(showing_ID),
    Foreign Key(movie_ID) REFERENCES movie_info(movie_ID),
	Foreign Key(screen_ID) REFERENCES screens(screen_ID)
);


 INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
 VALUES 
 (1, "The Movie", "2:19:00", "12A"),
 (2, "The Other Movie", "1:30:00", "15"),
 (3, "The 3D Amazing Movie",  "1:42:00", "PG"),
 (4, "La Allure", "1:09:00", "18"),
 (5, "The Cartoon", "1:15:00", "U"),
 (6, "The Scary Cartoon", "1:23:00", "PG"),
 (7, "The Coming Of Age", "1:40:00", "12A"),
 (8, "The War", "2:07:00", "15"),
 (9, "The Murder Mystery", "1:47:00", "15");

 INSERT INTO screens(screen_ID, four_k)
 VALUES 
  (1, True),
  (2, False),
  (3, True),
  (4, True),
  (5, True),
  (6, True),
  (7, True),
  (8, False),
  (9, True),
  (10, True);

 INSERT INTO showings(showing_ID, movie_ID,screen_ID, start_time, available_seats)
 VALUES 
  (1, 1, 2, '12:00:00', 10), 
  (2, 1, 2, '17:00:00', 23), 
  (3, 2, 9, '10:30:00', 30), 
  (4, 3, 1, '07:00:00', 38), 
  (5, 3, 5, '10:00:00', 26), 
  (6, 3, 1, '17:00:00', 5), 
  (7, 3, 1, '19:00:00', 0), 
  (8, 3, 5, '14:00:00', 2), 
  (9, 4, 9, '20:00:00', 14), 
  (10, 4, 9, '23:00:00', 23), 
  (11, 5, 6, '09:30:00', 30), 
  (12, 5, 6, '12:30:00', 7), 
  (13, 5, 6, '14:30:00', 0), 
  (14, 5, 6, '15:20:00', 0), 
  (15, 6, 10, '10:00:00', 32), 
  (16, 6, 10, '13:30:00', 25), 
  (17, 6, 10, '17:00:00', 14), 
  (18, 7, 7, '12:00:00', 36), 
  (19, 8, 4, '15:00:00', 24), 
  (20, 9, 3, '17:00:00', 0);


-- 4.2    Write a query to return the name and time of all movies that play after
--            12:00 given there is at least 1 available seat. Display the results in time
--            order.

SELECT m.movie_name, s.start_time
FROM movie_info AS m
INNER JOIN showings AS s
ON m.movie_id = s.movie_id
WHERE s.start_time > '12:00:00'
AND s.available_seats >= 1;

-- 4.3    Return the name of the movie with the most showings.


SELECT movie_name, COUNT(movie_name) AS count FROM 
(SELECT m.movie_name
FROM movie_info AS m
INNER JOIN showings AS s
ON m.movie_id = s.movie_id)

AS most_showings
GROUP BY m.movie_name
ORDER BY count desc
LIMIT 1




.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
    FROM students AS a, students AS b
    WHERE a.song = b.song and a.pet = b.pet and a.time < b.time;

CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest
  HAVING (SELECT COUNT(smallest) as count) = 1
  ORDER BY smallest;
CREATE DATABASE swell_wave;

USE swell_wave;

CREATE TABLE swelldata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    swell_wave_height FLOAT,
    swell_wave_direction FLOAT,
    swell_wave_period FLOAT,
    swell_wave_peak_period FLOAT,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

SELECT * FROM swelldata;


-- Since the data types are float, query them like this:

SELECT * FROM SwellData 
WHERE latitude BETWEEN 7.10321 AND 7.10341 
AND longitude BETWEEN 125.7189 AND 125.7191;


SELECT * FROM SwellData 
WHERE latitude BETWEEN 54.544487 AND 54.544687 
AND longitude BETWEEN 10.227387 AND 10.227587;
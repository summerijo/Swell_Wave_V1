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

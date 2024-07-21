-- myproject/queries.sql

CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    date VARCHAR(8),
    max_temp INTEGER,
    min_temp INTEGER,
    precipitation INTEGER
);

SELECT id FROM weather_data WHERE filename = %s AND date = %s;

INSERT INTO weather_data (filename, date, max_temp, min_temp, precipitation)
VALUES (%s, %s, %s, %s, %s);



-- Create the weather_stats table if it doesn't exist
CREATE TABLE IF NOT EXISTS weather_stats (
    id SERIAL PRIMARY KEY,
    year VARCHAR(4),
    filename VARCHAR(255),
    avg_max_temp FLOAT,
    avg_min_temp FLOAT,
    sum_precipitation INTEGER
);


INSERT INTO weather_stats (year, filename, avg_max_temp, avg_min_temp, sum_precipitation)
SELECT 
    SUBSTRING(date FROM 1 FOR 4)::VARCHAR AS year, 
    filename,
    AVG(max_temp)::FLOAT AS avg_max_temperature,
    AVG(min_temp)::FLOAT AS avg_min_temp, 
    SUM(precipitation) AS sum_precipitation 
FROM 
    weather_data 
GROUP BY 
    year, filename 
ORDER BY 
    year;

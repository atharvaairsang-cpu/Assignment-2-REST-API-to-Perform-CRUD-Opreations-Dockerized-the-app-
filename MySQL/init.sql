USE demodb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    wind_speed FLOAT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (city, country, temperature, humidity, wind_speed) VALUES
    ('New York', 'USA', 25.5, 60.0, 12.3),
    ('Los Angeles', 'USA', 30.2, 45.0, 8.1),
    ('Chicago', 'USA', 20.1, 55.0, 15.7),
    ('London', 'UK', 16.8, 70.0, 18.4),
    ('Paris', 'France', 19.3, 65.0, 10.2),
    ('Tokyo', 'Japan', 27.6, 75.0, 9.8),
    ('Mumbai', 'India', 32.1, 80.0, 14.5),
    ('Sydney', 'Australia', 22.4, 58.0, 20.1);

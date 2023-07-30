-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS temp_f_avg FROM hbtn_0c_0.temperatures GROUP BY city ORDER BY temp_f_avg DESC;

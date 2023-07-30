-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS ftemp_avg FROM temperatures GROUP BY city ORDER BY ftemp_avg DESC;

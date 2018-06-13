# Write your MySQL query statement below
SELECT w2.Id Id
FROM Weather w1, Weather w2
WHERE w2.RecordDATE = DATE_ADD(w1.RecordDATE, INTERVAL 1 DAY) AND w2.Temperature > w1.Temperature;

SELECT
    weather.id AS 'Id'
FROM
    weather
        JOIN
    weather w ON DATEDIFF(weather.date, w.date) = 1
        AND weather.Temperature > w.Temperature
;
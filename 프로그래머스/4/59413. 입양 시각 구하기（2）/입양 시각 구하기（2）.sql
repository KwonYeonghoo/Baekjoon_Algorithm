-- 코드를 입력하세요

WITH RECURSIVE HOURS AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1
    FROM HOURS
    WHERE HOUR < 23
),
sub AS(
    SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR(DATETIME)
    ORDER BY HOUR
)

SELECT h.HOUR, IFNULL(sub.COUNT, 0) COUNT
FROM HOURS h LEFT JOIN sub ON h.HOUR = sub.HOUR 
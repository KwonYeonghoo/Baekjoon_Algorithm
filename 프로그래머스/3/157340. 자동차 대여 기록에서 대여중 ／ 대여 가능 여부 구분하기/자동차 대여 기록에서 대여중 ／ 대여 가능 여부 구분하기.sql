-- 코드를 입력하세요
WITH available_cars AS (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE "2022-10-16" BETWEEN START_DATE AND END_DATE    
)

SELECT DISTINCT CAR_ID, 
    CASE
        WHEN CAR_ID in (SELECT * FROM available_cars) THEN '대여중'
        ELSE '대여 가능'
        END as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC
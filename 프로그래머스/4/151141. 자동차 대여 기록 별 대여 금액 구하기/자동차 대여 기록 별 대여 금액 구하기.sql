-- 코드를 입력하세요

# 자동차 종류가 트럭인 자동차의 대여 기록
# 대여 기록 별로 대여기록ID, 대여금액

WITH history AS (
    SELECT 
        crh.HISTORY_ID,
        crh.CAR_ID,
        cr.CAR_TYPE,
        cr.DAILY_FEE,
        DATEDIFF(crh.END_DATE, crh.START_DATE)+1 AS RENT_DATE,
        CASE
            WHEN DATEDIFF(crh.END_DATE, crh.START_DATE)+1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(crh.END_DATE, crh.START_DATE)+1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(crh.END_DATE, crh.START_DATE)+1 >= 7 THEN '7일 이상'
            ELSE "해당 없음"
            END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY crh JOIN CAR_RENTAL_COMPANY_CAR cr
        ON crh.CAR_ID = cr.CAR_ID
    WHERE cr.CAR_TYPE = '트럭'
)

SELECT
    history.HISTORY_ID,
    CASE history.DURATION_TYPE
        WHEN "해당 없음" THEN history.DAILY_FEE * history.RENT_DATE
        ELSE FLOOR(history.DAILY_FEE * history.RENT_DATE * (1 - dp.DISCOUNT_RATE*0.01))
    END AS FEE
FROM history LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp
    ON history.CAR_TYPE = dp.CAR_TYPE
        AND history.DURATION_TYPE = dp.DURATION_TYPE
ORDER BY FEE DESC, history.HISTORY_ID DESC
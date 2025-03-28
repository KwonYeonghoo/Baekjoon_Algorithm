-- 코드를 입력하세요
# 네비게이션 옵션이 포함된 자동차 리스트

SELECT *
FROM CAR_RENTAL_COMPANY_CAR
WHERE FIND_IN_SET('네비게이션', OPTIONS) > 0
ORDER BY CAR_ID DESC
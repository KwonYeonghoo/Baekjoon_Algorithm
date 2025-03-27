-- 코드를 입력하세요

# 상반기: 같은 맛 = 같은 공장 보장 O
# 7월: 같은 맛 = 같은 공장 보장 X

# 7월 총 주문량 + 상반기 총 주문량 상위 3가지 맛
# 7월은 맛별로 GROUP BY 필요

WITH july AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
)

SELECT fh.FLAVOR
FROM FIRST_HALF fh LEFT JOIN july ON fh.FLAVOR = july.FLAVOR
ORDER BY (fh.TOTAL_ORDER + july.TOTAL_ORDER) DESC
LIMIT 3

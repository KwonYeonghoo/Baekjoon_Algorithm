-- 코드를 입력하세요
# 년, 월 (ONLINE_SALE.SALES_DATE), 성별(USER_INFO.GENDER) 별로
# 상품을 구매한 회원수 집계
# 성별 없는 경우 결과에서 제외


SELECT YEAR(os.SALES_DATE) YEAR, MONTH(os.SALES_DATE) MONTH, ui.GENDER GENDER, COUNT(DISTINCT ui.USER_ID) as USERS
FROM ONLINE_SALE os LEFT JOIN USER_INFO ui ON os.USER_ID = ui.USER_ID
WHERE ui.GENDER IS NOT NULL
GROUP BY YEAR(os.SALES_DATE), MONTH(os.SALES_DATE), ui.GENDER
ORDER BY YEAR, MONTH, GENDER
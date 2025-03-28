-- 코드를 입력하세요
# 2022-10-05 등록된 게시물
# 게시글ID, 작성자 ID, 게시글 제목, 가격, 거래 상태
# SALE: 판매중
# RESERVED: 예약중
# DONE: 거래완료

SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, 
    CASE STATUS
        WHEN 'SALE' THEN '판매중'
        WHEN 'RESERVED' THEN '예약중'
        WHEN 'DONE' THEN '거래완료'
    END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC


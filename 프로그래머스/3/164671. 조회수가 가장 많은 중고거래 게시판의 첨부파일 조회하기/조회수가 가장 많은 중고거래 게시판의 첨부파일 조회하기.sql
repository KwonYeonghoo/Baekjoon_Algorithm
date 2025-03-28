-- 코드를 입력하세요

# 조회수가 가장 높은 중고거래 게시물
# 에 대한 첨부파일 경로를 조회 (/home/grep/src/게시글ID/파일ID 파일이름 확장자)

# 1. 조회수가 가장 높은 게시물 CTE로 구해놓기

WITH most_viewed AS (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
)

SELECT CONCAT("/home/grep/src/", BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (SELECT * FROM most_viewed)
ORDER BY FILE_PATH DESC
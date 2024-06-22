-- 코드를 입력하세요
SELECT board.title as title, board.board_id as board, reply.reply_id as reply_id, reply.writer_id as writer_id, reply.contents as contents, date_format(reply.created_date, "%Y-%m-%d") as created_date
from used_goods_board as board join used_goods_reply as reply 
        on board.board_id = reply.board_id
where board.created_date between "2022-10-01" and "2022-10-31"
order by created_date, title;
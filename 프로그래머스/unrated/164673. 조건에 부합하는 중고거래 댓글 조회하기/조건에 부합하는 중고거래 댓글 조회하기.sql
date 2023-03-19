-- 코드를 입력하세요
# 2022년 10월에 작성된 
# 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회
# 댓글 작성일을 기준으로 오름차순 정렬 
# 작성일이 같다면 게시글 제목을 기준 

SELECT a.TITLE, a.BOARD_ID, 
b.REPLY_ID, b.WRITER_ID	, b.CONTENTS, 
DATE_FORMAT(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD a
JOIN USED_GOODS_REPLY b ON a.BOARD_ID = b.BOARD_ID
WHERE a.CREATED_DATE LIKE '2022-10%'
ORDER BY b.CREATED_DATE, a.TITLE
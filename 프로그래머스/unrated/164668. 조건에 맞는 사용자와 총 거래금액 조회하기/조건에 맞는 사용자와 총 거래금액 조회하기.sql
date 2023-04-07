-- 완료된 중고 거래의 총금액이 70만 원 이상
-- 총거래금액을 기준으로 오름차순 

SELECT USER_ID, NICKNAME, sum(PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD b
LEFT JOIN USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
WHERE STATUS = 'DONE'
GROUP BY USER_ID
HAVING sum(PRICE) >= 700000
ORDER BY TOTAL_SALES 
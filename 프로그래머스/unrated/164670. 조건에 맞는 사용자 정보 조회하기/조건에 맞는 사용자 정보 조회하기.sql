-- 코드를 입력하세요
# 중고 거래 게시물을 3건 이상 등록한 사용자
# 사용자 ID, 닉네임, 전체주소, 전화번호 
# 전체 주소는 시, 도로명 주소, 상세 주소
# 전화번호의 경우 xxx-xxxx-xxxx 같은 형태
# 회원 ID를 기준 내림차순 

WITH over3 AS (
    select WRITER_ID, count(BOARD_ID) as CNT 
    from USED_GOODS_BOARD 
    group by WRITER_ID 
    having CNT >=3 
)


SELECT u.USER_ID, u.NICKNAME, 
    CONCAT(u.CITY, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) as 전체주소,
    CONCAT(substr(TLNO,1,3),'-',substr(TLNO,4,4),'-',substr(TLNO,8,4) ) as 전화번호 
FROM over3 o
LEFT JOIN USED_GOODS_USER u ON o.WRITER_ID = u.USER_ID 
ORDER BY USER_ID desc 
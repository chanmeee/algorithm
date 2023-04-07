-- 1) 2) 
-- 게시물을 3건 이상 등록 // 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
-- 주소는 시, 도로명 주소, 상세 주소가 함께 출력
-- 전화번호: - 하이픈 삽입 xxx-xxxx-xxxx 같은 형태
-- 회원 ID 내림차순 

# 1) 3건 이상 쓴 사람 찾기
# 2) 해당 사람의 정보 조회 (주소/전번 형태 유의)
# 3) 정렬 
WITH over3 AS(
    SELECT WRITER_ID, count(*) as CNT 
    FROM USED_GOODS_BOARD 
    GROUP BY WRITER_ID
    HAVING CNT >= 3 
)

SELECT u.USER_ID, NICKNAME, 
   concat(CITY,' ', STREET_ADDRESS1,' ', STREET_ADDRESS2)  as 전체주소,
   concat(substr(TLNO, 1,3),'-',substr(TLNO,4,4),'-',substr(TLNO,8,4)) as 전화번호
FROM over3 
LEFT JOIN USED_GOODS_USER u ON over3.WRITER_ID = u.USER_ID
ORDER BY USER_ID desc

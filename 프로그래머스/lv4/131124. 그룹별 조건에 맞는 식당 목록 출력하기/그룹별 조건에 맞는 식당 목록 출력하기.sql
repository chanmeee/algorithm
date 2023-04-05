-- 리뷰를 가장 많이 작성한 회원 
-- 리뷰들 조회 
-- 리뷰 작성일 기준 오름차순, 리뷰 텍스트 기준 오름차순

# 1) 리뷰 가장 많은 회원 찾기 -- 임시테이블 
# 2) 1테이블 기준 INNER JOIN 
WITH best_reviewer AS(
    SELECT MEMBER_ID, count(REVIEW_ID) as CNT
    FROM REST_REVIEW 
    GROUP BY MEMBER_ID 
    ORDER BY CNT desc
    LIMIT 1 
)

SELECT p.MEMBER_NAME, r.REVIEW_TEXT, 
        date_format(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM best_reviewer br
INNER JOIN MEMBER_PROFILE p ON br.MEMBER_ID = p.MEMBER_ID
INNER JOIN REST_REVIEW r ON r.MEMBER_ID = p.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT
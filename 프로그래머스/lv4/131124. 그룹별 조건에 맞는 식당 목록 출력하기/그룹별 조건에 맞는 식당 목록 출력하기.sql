-- cte : 리뷰를 가장 많이 작성한 회원 
-- 회원의 리뷰들을 조회 (회원 이름, 리뷰 텍스트, 리뷰 작성일)
-- 리뷰 작성일 오름차순, 리뷰 텍스트 오름차순

WITH topreview AS (
    select MEMBER_ID, COUNT(REVIEW_ID) as N_REVIEW 
    from REST_REVIEW 
    group by MEMBER_ID 
    order by N_REVIEW desc 
    LIMIT 1 
) 


SELECT MEMBER_NAME, REVIEW_TEXT, 
        date_format(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE 
FROM topreview t 
INNER JOIN MEMBER_PROFILE mp ON t.MEMBER_ID = mp.MEMBER_ID 
INNER JOIN REST_REVIEW  r ON t.MEMBER_ID = r.MEMBER_ID 
ORDER BY REVIEW_DATE, REVIEW_TEXT 


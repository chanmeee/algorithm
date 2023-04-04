-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
-- 회원 이름, 리뷰 텍스트, 리뷰 작성일
-- 리뷰 작성일을 기준 오름차순, 리뷰 텍스트 기준 오름차순
WITH most_reviews AS(
    SELECT member_id, review_text, review_date,
            count(*) AS reviews
    FROM rest_review  r
    GROUP BY member_id
    ORDER BY reviews desc
    LIMIT 1 
)

SELECT m.MEMBER_NAME, r.REVIEW_TEXT,
    date_format(r.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
    
FROM most_reviews as mr
INNER JOIN MEMBER_PROFILE as m  ON mr.member_id = m.member_id
INNER JOIN REST_REVIEW as r  ON m.member_id = r.member_id

ORDER BY REVIEW_DATE, REVIEW_TEXT 

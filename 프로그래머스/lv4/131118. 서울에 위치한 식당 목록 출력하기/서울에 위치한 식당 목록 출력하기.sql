-- 서울 위치 
-- 리뷰 평균점수는 소수점 세 번째 자리에서 반올림
-- 평균점수를 내림차순, 즐겨찾기수 내림차순
SELECT a.REST_ID, b.REST_NAME, b.FOOD_TYPE, b.FAVORITES, b.ADDRESS,
       round(avg(REVIEW_SCORE),2) as SCORE  
FROM REST_REVIEW  a 
JOIN REST_INFO  b ON a.REST_ID = b.REST_ID
GROUP BY a.REST_ID 
HAVING b.ADDRESS LIKE '서울%'
ORDER BY SCORE desc, b.FAVORITES desc 
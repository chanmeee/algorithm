-- 서울에 위치한 식당들
-- 리뷰 평균점수 : 소수점 세 번째 자리에서 반올림 
-- 평균점수를 기준으로 내림차순, 즐겨찾기수 기준 내림차순 
SELECT r.REST_ID,REST_NAME,FOOD_TYPE,FAVORITES,ADDRESS,
    round(avg(REVIEW_SCORE),2) as SCORE 
FROM REST_INFO  i
RIGHT JOIN REST_REVIEW  r  ON r.REST_ID=i.REST_ID 
WHERE ADDRESS LIKE '서울%'
GROUP BY r.REST_ID 
ORDER BY SCORE desc, FAVORITES desc
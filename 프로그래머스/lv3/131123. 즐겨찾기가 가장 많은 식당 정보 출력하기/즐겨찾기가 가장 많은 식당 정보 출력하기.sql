-- 음식종류별로 즐겨찾기수가 가장 많은 식당
-- 음식 종류를 기준으로 내림차순

WITH rank_by_foodtype AS(
    SELECT *,
    RANK() OVER (PARTITION BY FOOD_TYPE order by FAVORITES desc) as RNK 
    FROM REST_INFO 
)


SELECT FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
FROM rank_by_foodtype 
WHERE RNK = 1 
ORDER BY FOOD_TYPE desc


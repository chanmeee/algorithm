-- 코드를 입력하세요

# 음식종류별로 즐겨찾기수가 가장 많은 식당
WITH top AS (
    select *, rank () over (partition by FOOD_TYPE order by FAVORITES desc) as RNK 
    from REST_INFO 
) 

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES 
FROM top 
WHERE RNK =1
ORDER BY FOOD_TYPE desc

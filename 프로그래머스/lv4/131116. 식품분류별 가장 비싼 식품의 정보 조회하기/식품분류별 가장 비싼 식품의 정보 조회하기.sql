-- 식품분류별로 가격이 제일 비싼 식품
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 식품 가격을 기준으로 내림차순 
WITh t as (
    SELECT CATEGORY, PRICE, PRODUCT_NAME,
    rank() over (partition by CATEGORY order by PRICE desc) as RNK  
    FROM FOOD_PRODUCT 
    WHERE CATEGORY REGEXP '^(과자|국|김치|식용유)$' 
)

SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
FROM t 
WHERE RNK =1
ORDER BY PRICE desc
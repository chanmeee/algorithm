-- PRODUCT_ID: 외래키 
-- 필터링: 생산일자가 2022년 5월인 식품들
-- 식품 ID, 식품 이름, 총매출을 조회 
-- 정렬: 총매출을 기준으로 내림차순, 식품 ID를 기준으로 오름차순 

SELECT p.PRODUCT_ID, p.PRODUCT_NAME, 
        (p.PRICE*sum(o.AMOUNT)) as TOTAL_SALES 
FROM FOOD_ORDER o 
LEFT JOIN FOOD_PRODUCT p ON p.PRODUCT_ID = o.PRODUCT_ID 
WHERE o.PRODUCE_DATE LIKE '2022-05%'
GROUP BY p.PRODUCT_ID 
ORDER BY TOTAL_SALES desc, p.PRODUCT_ID
-- 총주문량> 3,000 & 주 성분이 과일
-- 아이스크림의 맛 
-- 총주문량이 큰 순서대로 
SELECT a.FLAVOR
FROM FIRST_HALF  a
LEFT JOIN ICECREAM_INFO  b ON a.FLAVOR = b.FLAVOR 
WHERE TOTAL_ORDER > 3000 and INGREDIENT_TYPE ='fruit_based'
ORDER BY TOTAL_ORDER desc
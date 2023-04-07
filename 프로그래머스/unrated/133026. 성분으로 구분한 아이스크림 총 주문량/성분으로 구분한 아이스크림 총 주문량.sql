-- FIRST_HALF : FLAVOR 기본키, INGREDIENT_TYPE : FLAVOR 기본키&외래키 
-- 상반기 동안 
-- 성분 타입과 성분 타입별 총주문량 
-- 총주문량 작은 순서대로  

SELECT i.INGREDIENT_TYPE, 
        sum(TOTAL_ORDER) as TOTAL_ORDER
FROM FIRST_HALF fh 
INNER JOIN ICECREAM_INFO i  ON fh.FLAVOR = i.FLAVOR 
GROUP BY i.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER 

#sugar_based 	13400
#fruit_based	5550
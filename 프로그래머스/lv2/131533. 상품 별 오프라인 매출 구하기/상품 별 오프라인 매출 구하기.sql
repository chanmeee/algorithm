-- 코드를 입력하세요
-- PRODUCT , OFFLINE_SALE  
-- 상품코드 별 매출액(판매가 * 판매량) 합계
-- 매출액을 기준으로 내림차순, 상품코드를 기준으로 오름차순 

SELECT PRODUCT_CODE,
       (p.PRICE * sum(off.SALES_AMOUNT)) as SALES 
FROM PRODUCT p
RIGHT JOIN OFFLINE_SALE  off on p.PRODUCT_ID = off.PRODUCT_ID 
GROUP BY p.PRODUCT_CODE
ORDER BY SALES desc, PRODUCT_CODE
-- 2022년 3월 
-- OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
-- 판매일 오름차순, 상품 ID 오름차순, 유저 ID 오름차순

WITH merged AS(
    select SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    from ONLINE_SALE 
    UNION ALL
    select SALES_DATE, PRODUCT_ID, NULL as USER_ID, SALES_AMOUNT
    from OFFLINE_SALE 
)

SELECT date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM  merged 
WHERE SALES_DATE LIKE '2022-03%'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID 

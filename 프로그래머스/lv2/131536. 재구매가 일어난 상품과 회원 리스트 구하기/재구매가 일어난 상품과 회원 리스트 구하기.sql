-- 코드를 입력하세요
SELECT * 
FROM (SELECT USER_ID, PRODUCT_ID 
        FROM ONLINE_SALE  
        GROUP BY USER_ID, PRODUCT_ID 
        HAVING count(*) >= 2 ) a 
ORDER BY a.USER_ID, a.PRODUCT_ID desc 
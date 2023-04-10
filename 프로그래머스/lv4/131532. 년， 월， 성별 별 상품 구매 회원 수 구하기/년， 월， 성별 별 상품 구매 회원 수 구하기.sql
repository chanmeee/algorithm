-- 년, 월, 성별 별로 상품을 구매한 회원수
-- 년, 월, 성별을 기준으로 오름차순
-- 성별 정보가 없는 경우 결과에서 제외
SELECT year(SALES_DATE) as YEAR, month(SALES_DATE) as MONTH, GENDER,
        count(distinct s.USER_ID) as USERS  
FROM ONLINE_SALE  s
LEFT JOIN USER_INFO ui ON s.USER_ID=ui.USER_ID 
WHERE GENDER is not null 
GROUP BY YEAR,MONTH,GENDER
ORDER BY YEAR,MONTH,GENDER
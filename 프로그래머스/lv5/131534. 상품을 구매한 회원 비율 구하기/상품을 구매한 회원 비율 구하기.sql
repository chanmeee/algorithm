-- USER_ID : 외래키 
-- 필터링 :  2021년에 가입 
-- 상품 구매한 회원수, 회원비율(두번째자리에서 반올림)
-- 년, 월 별로 출력 
-- 년을 기준으로 오름차순, 월 기준 오름차순 

# 1) 회원 수, 구입 여부, 년, 월 변수 - 임시테이블 
# 2) 그룹핑 : 연, 월 -> 회원수 sum, 구입회원수 sum
# 3) 회원비율 계산 
# 4) 정렬 
WITH ym AS(
    SELECT DISTINCT u.user_id,
            year(s.sales_date) as YEAR, month(s.sales_date) as MONTH
    FROM USER_INFO  u 
    JOIN ONLINE_SALE s ON u.USER_ID = s.USER_ID 
    WHERE u.JOINED LIKE '2021-%'
)

SELECT year, month,
        count(*) as PUCHASED_USERS,
        round(count(*)/(select count(*) from user_info where year(joined)=2021), 1) as PUCHASED_RATIO
FROM ym 
GROUP BY year, month 
ORDER BY year, month 


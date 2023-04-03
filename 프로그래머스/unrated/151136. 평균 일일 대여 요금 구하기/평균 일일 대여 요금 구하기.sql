-- 자동차 종류가 'SUV'
-- 평균 일일 대여 요금, 소수 첫 번째 자리에서 반올림 
-- AVERAGE_FEE  
SELECT round(avg(DAILY_FEE),0) as AVERAGE_FEE 
FROM CAR_RENTAL_COMPANY_CAR 
WHERE CAR_TYPE = 'SUV'
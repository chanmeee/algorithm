-- 평균 대여 기간이 7일 이상인 자동차들 
-- 자동차 ID와 평균 대여 기간 
-- 평균 대여 기간은 소수점 두번째 자리에서 반올림 
-- 평균 대여 기간 내림차순, 자동차 ID 내림차순
WITH dur_table AS(
    SELECT CAR_ID, 
            timestampdiff(day, START_DATE, END_DATE)+1 as DURATION 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  
) 


SELECT CAR_ID, round(avg(DURATION),1) as AVERAGE_DURATION 
FROM dur_table 
GROUP BY CAR_ID 
HAVING AVERAGE_DURATION >= 7 
ORDER BY AVERAGE_DURATION desc, CAR_ID desc 

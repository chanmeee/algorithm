-- 대여 시작일을 기준으로 총 대여 횟수가 5회 이상인 자동차
-- 월 별 자동차 ID별 총 대여 횟수 
-- 월 오름차순, 자동차 ID 내림차순으로 정렬
with T as (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  
    WHERE START_DATE between '2022-08-01' and '2022-10-31'
    GROUP BY CAR_ID
    HAVING count(CAR_ID) >=5 
)

SELECT month(start_date) as MONTH, CAR_ID, count(CAR_ID) as RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY rh 
WHERE START_DATE between '2022-08-01' and '2022-10-31'
    and CAR_ID in (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY  
    WHERE START_DATE between '2022-08-01' and '2022-10-31'
    GROUP BY CAR_ID
    HAVING count(CAR_ID) >=5 
)
GROUP BY MONTH, car_id
ORDER BY MONTH, CAR_ID desc
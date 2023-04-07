-- AVAILABILITY 컬럼 추가 : 반납 날짜가 2022년 10월 16일인 경우도 '대여중'
-- 자동차 ID를 기준으로 내림차순  
WITH temp AS(
    SELECT CAR_ID,
    case when '2022-10-16' between START_DATE and END_DATE then 1
    else 0
    end as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
) 

SELECT CAR_ID,
    case when sum(AVAILABILITY)>0 then '대여중'
    else '대여 가능' end as AVAILABILITY 
FROM temp
GROUP BY CAR_ID
ORDER BY CAR_ID desc
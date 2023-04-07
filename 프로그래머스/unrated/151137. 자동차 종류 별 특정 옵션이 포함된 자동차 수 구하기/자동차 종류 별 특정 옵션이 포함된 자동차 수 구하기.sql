-- 하나 이상의 옵션이 포함된 자동차
-- 자동차 종류 별로 몇 대 
-- 종류를 기준으로 오름차순
SELECT CAR_TYPE, count(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR  
WHERE OPTIONS REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE
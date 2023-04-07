-- 종류가 '트럭'
-- 대여 기록 별로 대여 금액
-- 대여 금액을 기준으로 내림차순, 대여 기록 ID를 기준으로 내림차순

# WITH newrh as (
#     SELECT HISTORY_ID, CAR_TYPE,
#     DAILY_FEE*(timestampdiff(day, START_DATE, END_DATE)+1) as ORI_FEE,
#     CASE 
#     WHEN timestampdiff(day, START_DATE, END_DATE)+1 < 7 THEN null 
#     WHEN timestampdiff(day, START_DATE, END_DATE)+1 < 30 THEN '7일 이상'
#     WHEN timestampdiff(day, START_DATE, END_DATE)+1 >= 90 THEN '30일 이상'
#     ELSE '90일 이상'
#     END as DURATION_TYPE 
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY rh 
#     LEFT JOIN CAR_RENTAL_COMPANY_CAR c  ON rh.CAR_ID = c.CAR_ID 
#     WHERE CAR_TYPE = '트럭' 
# ) 

# SELECT rh.HISTORY_ID, 
#     round(ORI_FEE*(100-ifnull(discount_rate,0))/100,0) as FEE 
# FROM newrh rh
# LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d ON d.CAR_TYPE = rh.CAR_TYPE and d.DURATION_TYPE= rh.DURATION_TYPE	
# ORDER BY FEE desc, HISTORY_ID desc 

with T as (
    select 
        HISTORY_ID, 
        car_type, 
        (datediff(end_date, start_date)+1)*daily_fee as fee,
        case 
            when datediff(end_date, start_date)+1 < 7 then null
            when datediff(end_date, start_date)+1 < 30 then '7일 이상' 
            when datediff(end_date, start_date)+1 < 90 then '30일 이상'
            else '90일 이상'
        end duration_type
    from 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY a 
        join 
        CAR_RENTAL_COMPANY_CAR b 
        on a.car_id=b.car_id
    where 
        car_type='트럭'
)

SELECT 
    history_id, 
    fee * (100-ifnull(discount_rate, 0)) div 100 fee
from 
    t left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN b 
    on t.car_type=b.car_type and t.duration_type=b.duration_type
order by 
    2 desc, 1 desc
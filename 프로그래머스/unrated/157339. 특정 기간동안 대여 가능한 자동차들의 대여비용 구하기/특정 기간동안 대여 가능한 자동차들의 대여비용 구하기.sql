-- 코드를 입력하세요
WITH cars AS (
    select c.CAR_ID, c.CAR_TYPE, 
            CAST((c.DAILY_FEE)*30* (100-d.DISCOUNT_RATE)*0.01 as signed integer) as FEE 
    from CAR_RENTAL_COMPANY_CAR c  
    left join (
        select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        where DURATION_TYPE = '30일 이상' ) d 
        ON c.CAR_TYPE = d.CAR_TYPE 
    where (c.CAR_TYPE IN ('세단','SUV') and 
        c.CAR_ID NOT IN (
            select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
            where END_DATE >='2022-11-01' and START_DATE <='2022-11-30'
            )
           )
    )

SELECT CAR_ID, CAR_TYPE, FEE 
FROM cars 
WHERE FEE BETWEEN 500000 and 2000000
ORDER BY FEE desc, CAR_TYPE, CAR_ID desc 
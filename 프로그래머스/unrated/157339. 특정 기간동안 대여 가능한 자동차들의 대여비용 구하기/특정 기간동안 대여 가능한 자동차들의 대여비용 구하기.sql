-- CAR_RENTAL_COMPANY_CAR : 대여 중인 자동차들
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY : 대여 기록 정보
-- CAR_RENTAL_COMPANY_DISCOUNT_PLAN : 할인 정책 

# 1) 출력할 컬럼 (3) : 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE)  
# 2) 필터링 조건 (3) 
## '세단' 또는 'SUV' 인 자동차 
## 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능 -> DUTAION_TYPE이 30일이상, 90일 이상 
## 30일간의 대여 금액이 50만원 이상 200만원 미만
# 3) 정렬 조건 (3)
## 대여 금액 기준 내림차순, 자동차 종류 기준 오름차순,  자동차 ID 기준 내림차순

# 1) 조건 맞는 자동차 type 필터링 후 , 자동차 id, 일일요금 열 선택 
# 2) 대여 기간 계산 -> 1)테이블과 inner join on 자동차 id 
# 3) 30일 대여 금액 계산 -> 대여 금액 필터링
# 4) 정렬 

WITH CANDI AS(

    select c.CAR_ID, c.CAR_TYPE, 
           CAST((c.DAILY_FEE*30)* (100-d.DISCOUNT_RATE)/100 as signed integer) as FEE 
    FROM CAR_RENTAL_COMPANY_CAR  c
    LEFT JOIN ( select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
               where duration_type = '30일 이상' )  d 
    ON c.CAR_TYPE = d.CAR_TYPE 
    WHERE c.CAR_TYPE in ('세단', 'SUV')
        and c.car_id not in (
            select car_id
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where end_date >= '2022-11-01' and start_date <= '2022-11-30'
        )
) 

        
SELECT CAR_ID, CAR_TYPE, FEE
FROM CANDI
WHERE FEE >=500000 and FEE <= 2000000
ORDER BY FEE desc, CAR_TYPE, CAR_ID desc 


-- 5월 1일을 기준 조회 
-- 출고여부: 5월 1일까지 출고완료, 이후 날짜는 출고 대기, 미정이면 출고미정 
-- 주문 ID를 기준으로 오름차순 
SELECT ORDER_ID,PRODUCT_ID,
    date_format(OUT_DATE,'%Y-%m-%d') as OUT_DATE,
    CASE WHEN OUT_DATE is null THEN '출고미정'
    WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
    ELSE '출고대기'
    END as 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID
-- 각 시간대별로 입양이 몇 건이나 발생
WITH RECURSIVE h_table AS (
    select 0 as HOUR
    UNION ALL 
    select hour+1 from h_table where hour<23
    # hour<23 때까지 h_table의 hour 변수에 1을 더한다 
)

SELECT h.hour, count(ANIMAL_ID) CNT
FROM h_table h
LEFT JOIN ANIMAL_OUTS ao ON h.hour = hour(ao.DATETIME) 
GROUP BY h.hour  
ORDER BY h.hour 

-- 0시부터 23시, 시간대별로 입양이 몇 건
-- 시간대 순으로 정렬
WITH RECURSIVE H_table AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM H_table where HOUR<23) 

SELECT h.HOUR as HOUR, count(ANIMAL_ID) as COUNT
FROM H_table h
LEFT JOIN ANIMAL_OUTS outs ON h.HOUR = hour(outs.DATETIME) 
GROUP BY h.HOUR
ORDER BY h.HOUR 
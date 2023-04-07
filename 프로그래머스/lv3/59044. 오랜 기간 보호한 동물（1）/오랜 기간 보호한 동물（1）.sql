-- 필터링: 아직 입양을 못 간 동물  (V) 
-- 가장 오래 보호소에 있었던 동물 3마리 -> 기간 계산 (timestampdiff, min)
-- 이름과 보호 시작일
-- 보호 시작일 순으로 조회  
SELECT ins.NAME, ins.DATETIME
FROM ANIMAL_INS ins
LEFT JOIN ANIMAL_OUTS outs ON ins.ANIMAL_ID = outs.ANIMAL_ID 
WHERE outs.DATETIME is null 
ORDER BY ins.DATETIME 
LIMIT 3 
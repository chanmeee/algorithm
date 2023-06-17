-- 아직 입양을 못 간 동물, 가장 오래 보호소에 있었던 동물 3마리
SELECT ins.NAME, ins.DATETIME 
FROM ANIMAL_INS ins 
LEFT JOIN ANIMAL_OUTS outs ON ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE outs.DATETIME IS NULL
ORDER BY ins.DATETIME 
LIMIT 3 
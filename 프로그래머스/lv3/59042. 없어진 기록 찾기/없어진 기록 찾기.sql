-- 코드를 입력하세요
-- ANIMAL_ID : 외래키 
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물 
-- 동물의 ID와 이름을 ID 순 
SELECT outs.ANIMAL_ID, outs.NAME 
FROM ANIMAL_OUTS outs
LEFT JOIN ANIMAL_INS ins ON ins.ANIMAL_ID = outs.ANIMAL_ID 
WHERE outs.DATETIME is not null and ins.DATETIME is null
ORDER BY outs.ANIMAL_ID, outs.NAME 


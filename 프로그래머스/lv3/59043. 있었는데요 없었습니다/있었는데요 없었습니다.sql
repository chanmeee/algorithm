-- ANIMAL_ID: 외래키 
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회
-- 보호 시작일이 빠른 순 
SELECT ins.ANIMAL_ID, ins.NAME 
FROM ANIMAL_INS ins
LEFT JOIN ANIMAL_OUTS outs ON ins.ANIMAL_ID = outs.ANIMAL_ID 
WHERE ins.DATETIME > outs.DATETIME 
ORDER BY ins.DATETIME
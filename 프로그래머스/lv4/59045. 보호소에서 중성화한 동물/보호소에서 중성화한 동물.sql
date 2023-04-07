-- ANIMAL_ID : 외래키 
-- 들어올 당시 중성화x & 나갈 당시 중성화o 
-- 동물의 아이디와 생물 종, 이름을 조회
-- 아이디 순 정렬 

# 1) 테이블 join / ins 기준 left 
# 2) where in때 중x, out때 중
# 3) select
# 4) order by 

SELECT ins.ANIMAL_ID, ins.ANIMAL_TYPE, ins.NAME 
FROM ANIMAL_INS ins
LEFT JOIN ANIMAL_OUTS outs ON ins.ANIMAL_ID = outs.ANIMAL_ID 
WHERE ins.SEX_UPON_INTAKE LIKE 'Intact%' and
       (outs.SEX_UPON_OUTCOME LIKE 'Spayed%' or 
        outs.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY ins.ANIMAL_ID
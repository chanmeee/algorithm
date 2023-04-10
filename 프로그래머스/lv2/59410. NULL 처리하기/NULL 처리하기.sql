-- 이름이 없는 동물의 이름은 "No name"
-- 아이디 순으로 조회 
SELECT ANIMAL_TYPE,
case when NAME is null then 'No name'
else NAME 
end as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS  
ORDER BY ANIMAL_ID 
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME , SEX_UPON_INTAKE
FROM  ANIMAL_INS 
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')

# SELECT ANIMAL_ID,NAME,SEX_UPON_INTAKE
# FROM ANIMAL_INS 
# WHERE NAME REGEXP 'Lucy|Ella|Pickle|Rogan|Sabrina|Mitty'
#WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')

# A373219	Ella	Spayed Female
# A377750	Lucy	Spayed Female
# A380009	Pickle	Spayed Female
# A395451	Rogan	Neutered Male
# A399421	Lucy	Spayed Female
# A400680	Lucy	Spayed Female
# A406756	Sabrina	Spayed Female
# A410684	Mitty	Spayed Female
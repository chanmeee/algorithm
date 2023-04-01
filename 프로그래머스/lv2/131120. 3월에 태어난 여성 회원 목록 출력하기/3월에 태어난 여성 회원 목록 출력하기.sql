-- 생일이 3월인 여성 회원 
-- ID, 이름, 성별, 생년월일
-- 전화번호가 NULL인 경우, 제외
-- 회원ID를 기준, 오름차순 정렬
SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
        date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE GENDER = 'W' and month(DATE_OF_BIRTH) = 3 and TLNO IS NOT NULL
ORDER BY MEMBER_ID 


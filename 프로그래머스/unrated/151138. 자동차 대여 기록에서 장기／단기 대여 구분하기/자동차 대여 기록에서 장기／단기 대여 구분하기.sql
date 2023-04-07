-- 대여 시작일이 2022년 9월
-- 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시
SELECT HISTORY_ID, CAR_ID,
date_format(START_DATE,'%Y-%m-%d') as START_DATE,
date_format(END_DATE,'%Y-%m-%d') as END_DATE,
CASE WHEN timestampdiff(day,START_DATE,END_DATE)+1 >=30
THEN '장기 대여' 
ELSE '단기 대여' END as RENT_TYPE 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID desc
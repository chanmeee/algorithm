-- 2022년 5월에 예약한 환자 수
-- 진료과코드 별로 조회
-- 환자 수 오름차순, 진료과코드 오름차순 

SELECT MCDP_CD as 진료과코드, count(PT_NO) as '5월예약건수'
FROM APPOINTMENT  
WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD 
ORDER BY 5월예약건수, 진료과코드 
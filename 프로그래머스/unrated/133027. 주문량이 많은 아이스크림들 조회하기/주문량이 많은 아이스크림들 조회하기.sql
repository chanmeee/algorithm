-- 7월 아이스크림 총 주문량 + 상반기의 아이스크림 총 주문량 => 상위 3개 맛
-- FIRST_HALF : FLAVOR는 기본 키 (유일), 
--              SHIPMENT_ID는 외래키 (외부테이블과 연결) 

# 1) JULY 를 group by flavor 
# 2) 1) JULY와 FIRST_HALF를 SHIPMENT_ID로 join 
# 3) total order 2 변수 계산 
# 4) 3)변수 내림차순 정렬 후 top3 flavor만 선택 

##############################
select fh.FLAVOR 
FROM FIRST_HALF fh 
JOIN (SELECT FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
     FROM JULY 
     GROUP BY FLAVOR ) j2  ON j2.FLAVOR = fh.FLAVOR 
ORDER BY (fh.TOTAL_ORDER + j2.TOTAL_ORDER) desc
LIMIT 3
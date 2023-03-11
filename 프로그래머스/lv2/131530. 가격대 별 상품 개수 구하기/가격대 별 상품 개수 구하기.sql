-- 코드를 입력하세요
# 만원 단위의 가격대 별로 상품 개수를 출력 
# PRICE_GROUP, PRODUCTS 변수명
# 가격대 기준 오름차순 정렬 
# 그룹 변수(ex. 나이대, 금액대) 만들 떄는 select에 CASE WHEN-THEN 명령어!

SELECT 
    TRUNCATE(PRICE, -4) as PRICE_GROUP,
    count(*) PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP
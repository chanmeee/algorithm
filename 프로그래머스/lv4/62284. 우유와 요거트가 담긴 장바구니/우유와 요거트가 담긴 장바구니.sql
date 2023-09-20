-- 코드를 입력하세요
SELECT CART_ID #, count(distinct NAME)
FROM CART_PRODUCTS  c 
WHERE NAME IN ('Milk', 'Yogurt')
GROUP BY CART_ID HAVING count(distinct NAME) = 2
ORDER BY CART_ID 
# 286
# 789
# # 977

# SELECT CART_ID, NAME
# FROM CART_PRODUCTS  c 
# WHERE NAME IN ('Milk', 'Yogurt')
# #GROUP BY CART_ID HAVING count(NAME) =2

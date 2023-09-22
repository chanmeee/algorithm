-- 코드를 입력하세요
# heavy_user table
WITH heavy_user AS (
    select HOST_ID, count(distinct NAME) CNT
    from PLACES 
    group by HOST_ID having count(distinct NAME)>=2 
)


SELECT *
FROM PLACES
WHERE HOST_ID in (
    select HOST_ID from heavy_user)
ORDER BY ID 


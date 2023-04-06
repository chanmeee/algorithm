-- '경제' 카테고리 
-- 출판일을 기준으로 오름차순  
SELECT b.BOOK_ID, a.AUTHOR_NAME, 
       date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK b
LEFT JOIN AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID 
WHERE b.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE 


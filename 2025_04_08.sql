-- https://school.programmers.co.kr/learn/courses/30/lessons/144855

SELECT CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B JOIN BOOK_SALES S
ON B.BOOK_ID = S.BOOK_ID
WHERE DATE_FORMAT(S.SALES_DATE,"%Y-%m")="2022-01"
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY ASC

-- https://school.programmers.co.kr/learn/courses/30/lessons/131123

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE,FAVORITES) IN (
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC, FAVORITES DESC
-- https://school.programmers.co.kr/learn/courses/30/lessons/151139#qna

WITH M5 AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE DATE_FORMAT(START_DATE, "%Y-%m") BETWEEN "2022-08" AND "2022-10"
    GROUP BY CAR_ID
    HAVING COUNT(HISTORY_ID)>=5
)
SELECT MONTH(START_DATE) AS MONTH, H.CAR_ID, COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H JOIN M5 ON H.CAR_ID = M5.CAR_ID
WHERE DATE_FORMAT(START_DATE, "%Y-%m") BETWEEN "2022-08" AND "2022-10"
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC

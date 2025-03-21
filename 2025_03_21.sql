-- https://school.programmers.co.kr/learn/courses/30/lessons/273709
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY="LEGEND"

-- https://school.programmers.co.kr/learn/courses/30/lessons/157342

SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE)+1),1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION>=7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC

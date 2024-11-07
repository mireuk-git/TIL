# https://school.programmers.co.kr/learn/courses/30/lessons/157339#qna

SELECT DISTINCT C.CAR_ID, C.CAR_TYPE, CONVERT(30*C.DAILY_FEE*(100-D.DISCOUNT_RATE)/100, SIGNED) AS FEE
FROM CAR_RENTAL_COMPANY_CAR C 
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D ON C.CAR_TYPE=D.CAR_TYPE 
WHERE C.CAR_TYPE IN ('세단','SUV')
AND DURATION_TYPE = '30일 이상'
AND C.CAR_ID NOT IN (
    SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE>='2022-11-01' AND START_DATE<='2022-11-30'
)
HAVING FEE>=500000 AND FEE<2000000
ORDER BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC
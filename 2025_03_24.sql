-- https://school.programmers.co.kr/learn/courses/30/lessons/151137

SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE "%시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC

-- https://school.programmers.co.kr/learn/courses/30/lessons/132202

SELECT MCDP_CD AS 진료과코드, COUNT(APNT_NO) AS 5월예약건수
FROM APPOINTMENT
WHERE MONTH(APNT_YMD)=5
GROUP BY 진료과코드
ORDER BY 5월예약건수, 진료과코드
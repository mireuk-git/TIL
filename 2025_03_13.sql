-- https://school.programmers.co.kr/learn/courses/30/lessons/299308

SELECT CONCAT(CEIL(MONTH(DIFFERENTIATION_DATE)/3),"Q") AS QUARTER,
COUNT(ID) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER

-- https://school.programmers.co.kr/learn/courses/30/lessons/298518

SELECT COUNT(F.ID) AS FISH_COUNT
FROM FISH_INFO F JOIN FISH_NAME_INFO N
ON F.FISH_TYPE = N.FISH_TYPE
WHERE N.FISH_NAME IN ('BASS','SNAPPER')
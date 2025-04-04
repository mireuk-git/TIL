-- https://school.programmers.co.kr/learn/courses/30/lessons/284527

WITH G AS(SELECT G1.EMP_NO, G1.SCORE+G2.SCORE AS SCORE
    FROM HR_GRADE G1 JOIN HR_GRADE G2
    ON G1.EMP_NO = G2.EMP_NO
    WHERE G1.YEAR=2022 AND G1.HALF_YEAR=1 AND G2.YEAR=2022 AND G2.HALF_YEAR=2)
SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM HR_EMPLOYEES E JOIN G
ON E.EMP_NO = G.EMP_NO
ORDER BY G.SCORE DESC
LIMIT 1

-- https://school.programmers.co.kr/learn/courses/30/lessons/276034

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE ((SELECT CODE FROM SKILLCODES WHERE NAME='PYTHON') | (SELECT CODE FROM SKILLCODES WHERE NAME='C#')) & SKILL_CODE
ORDER BY ID
-- https://school.programmers.co.kr/learn/courses/30/lessons/276036#qna

WITH SKILLS AS (
    SELECT 
    (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'Python') AS PYTHON,
    (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') AS FRONTEND,
    (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'C#') AS C)
,
CTE AS (SELECT CASE 
    WHEN SKILL_CODE & (SELECT PYTHON FROM SKILLS) > 0 AND SKILL_CODE && (SELECT FRONTEND FROM SKILLS) > 0 THEN "A"
    WHEN SKILL_CODE & (SELECT C FROM SKILLS) > 0 THEN "B"
    WHEN SKILL_CODE & (SELECT FRONTEND FROM SKILLS) > 0 THEN "C"
    END AS GRADE, ID, EMAIL
FROM DEVELOPERS)

SELECT * FROM CTE WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC


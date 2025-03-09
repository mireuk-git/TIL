-- https://school.programmers.co.kr/learn/courses/30/lessons/59407

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- https://school.programmers.co.kr/learn/courses/30/lessons/59410

SELECT ANIMAL_TYPE, CASE
    WHEN A.NAME IS NULL THEN "No name"
    ELSE A.NAME
    END AS NAME
, SEX_UPON_INTAKE
FROM ANIMAL_INS A
ORDER BY ANIMAL_ID

SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE
FROM ANIMAL_INS A
ORDER BY ANIMAL_ID

-- https://school.programmers.co.kr/learn/courses/30/lessons/59035

SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
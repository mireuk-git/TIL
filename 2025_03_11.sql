-- https://school.programmers.co.kr/learn/courses/30/lessons/301646
SELECT COUNT(GENOTYPE) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE%8 IN (1,4,5)

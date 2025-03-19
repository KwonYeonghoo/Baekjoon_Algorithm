-- 코드를 작성해주세요

-- ID 1인 개체의 자식은 ID 3
-- SELF JOIN

SELECT p.ID, COUNT(c.PARENT_ID) as CHILD_COUNT
FROM ECOLI_DATA as p LEFT JOIN ECOLI_DATA as c ON p.ID = c.PARENT_ID
GROUP BY p.ID
ORDER BY p.ID

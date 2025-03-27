-- 코드를 작성해주세요

# GRADE별 개발자의 정보 -> GRADE 컬럼을 정의해야겠지? CTE
# 

WITH grades AS (
    SELECT CASE 
            WHEN (d.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE SKILLCODES.NAME = 'Python') > 0)
                AND (d.SKILL_CODE & (SELECT BIT_OR(CODE) FROM SKILLCODES WHERE SKILLCODES.CATEGORY = 'Front End') > 0)
                    THEN 'A'
            WHEN (d.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE SKILLCODES.NAME = 'C#') > 0)
                    THEN 'B'
            WHEN (d.SKILL_CODE & (SELECT BIT_OR(CODE) FROM SKILLCODES WHERE SKILLCODES.CATEGORY = 'Front End') > 0)
                    THEN 'C'
            END AS GRADE,
        d.ID
    FROM DEVELOPERS d
)

SELECT g.GRADE, d.ID, d.EMAIL
FROM DEVELOPERS d JOIN grades g on d.ID = g.ID
WHERE g.GRADE IS NOT NULL
ORDER BY GRADE, d.ID
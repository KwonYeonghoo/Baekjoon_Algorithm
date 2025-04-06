-- 코드를 작성해주세요

# 사원별 성과금 정보
# 점수별 등급, 등급에 따른 성과금

WITH avg_grade AS (
    SELECT EMP_NO,
        CASE
            WHEN AVG(SCORE) >= 96 THEN '96 이상'
            WHEN AVG(SCORE) >= 90 THEN '90 이상'
            WHEN AVG(SCORE) >= 80 THEN '80 이상'
            ELSE '이외'
            END as CRITERIA_SCORE,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
            END as GRADE,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 0.2
            WHEN AVG(SCORE) >= 90 THEN 0.15
            WHEN AVG(SCORE) >= 80 THEN 0.1
            ELSE 0
            END as INCENTIVE
    FROM HR_GRADE
    GROUP BY EMP_NO, YEAR
)

SELECT he.EMP_NO, he.EMP_NAME, avg_grade.GRADE, he.SAL*avg_grade.INCENTIVE as BONUS
FROM HR_EMPLOYEES he LEFT JOIN avg_grade ON he.EMP_NO = avg_grade.EMP_NO

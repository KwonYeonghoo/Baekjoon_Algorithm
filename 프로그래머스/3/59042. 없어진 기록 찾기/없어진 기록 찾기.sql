-- 코드를 입력하세요

# 입양을 간 기록은 있는데, 보호소에 들어온 기록은 없다? 
# -> OUTS에는 ID가 있는데, INS에는 없다
# -> OUTS 기준으로 LEFT JOIN
# INS.ANIMAL_ID IS NULL

SELECT outs.ANIMAL_ID, outs.NAME
FROM ANIMAL_OUTS outs LEFT JOIN ANIMAL_INS ins ON outs.ANIMAL_ID = ins.ANIMAL_ID
WHERE ins.ANIMAL_ID IS NULL
ORDER BY outs.ANIMAL_ID
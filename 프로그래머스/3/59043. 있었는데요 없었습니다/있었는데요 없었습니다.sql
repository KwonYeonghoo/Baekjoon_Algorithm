-- 코드를 입력하세요
SELECT INS.animal_id, INS.name
FROM animal_ins INS join animal_outs OUTS
    on INS.animal_id = OUTS.animal_id
WHERE INS.datetime > OUTS.datetime
order by INS.datetime;
    
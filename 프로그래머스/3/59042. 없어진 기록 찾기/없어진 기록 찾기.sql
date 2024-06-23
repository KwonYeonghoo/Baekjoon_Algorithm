-- 코드를 입력하세요
SELECT OUTS.animal_id, OUTS.name
FROM animal_ins as INS right join animal_outs as OUTS
     on OUTS.animal_id = INS.animal_id
     WHERE INS.animal_id IS NULL
order by OUTS.animal_id;
-- 코드를 입력하세요
-- animal_ins에는 있지만 animal_outs에는 없는 동물들
SELECT INS.name, INS.datetime
FROM animal_ins INS left join animal_outs OUTS
     ON INS.animal_id = OUTS.animal_id
where OUTS.animal_id IS NULL
order by INS.datetime
limit 3;
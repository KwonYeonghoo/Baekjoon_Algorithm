-- 코드를 입력하세요
-- animal_ins에서는 intact, animal_outs에서는 neutered, spayed
SELECT INS.animal_id, INS.animal_type, INS.name
FROM animal_ins INS join animal_outs OUTS
     on INS.animal_id = OUTS.animal_id
where INS.SEX_UPON_INTAKE like "Intact%"
        and INS.SEX_UPON_INTAKE != OUTS.SEX_UPON_OUTCOME
order by INS.animal_id
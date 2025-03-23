-- 코드를 작성해주세요

SELECT COUNT(*) as FISH_COUNT
FROM (
    SELECT fi.FISH_TYPE, fni.FISH_NAME
    FROM FISH_INFO fi LEFT JOIN FISH_NAME_INFO fni ON fi.FISH_TYPE = fni.FISH_TYPE
    WHERE fni.FISH_NAME in ("BASS", "SNAPPER")
) jfi
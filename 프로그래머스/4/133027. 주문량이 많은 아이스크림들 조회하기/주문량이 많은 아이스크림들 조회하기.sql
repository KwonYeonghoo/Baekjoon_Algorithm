-- 코드를 입력하세요
SELECT FHJ.flavor
FROM (SELECT FH.flavor, SUM(FH.total_order + J.total_order) as combined_order
      FROM first_half FH join july J on FH.flavor = J.flavor
      GROUP BY FH.flavor) as FHJ
order by FHJ.combined_order desc
limit 3;
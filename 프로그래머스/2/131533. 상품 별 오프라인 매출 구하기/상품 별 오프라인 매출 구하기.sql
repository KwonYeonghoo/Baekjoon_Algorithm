-- 코드를 입력하세요
SELECT P.product_code, SUM(P.price * OS.sales_amount) as sales
from product P join offline_sale OS
     on P.product_id = OS.product_id
    group by P.product_code
order by sales desc, P.product_code asc;
-- https://leetcode.com/problems/sales-analysis-iii/

-- 如何使用 with as
-- 透過排除非條件內的資料來查詢 not in 

with cte as (
    select product_id
    from Sales
    where sale_date < "2019-01-01" or sale_date > "2019-03-31"
)

select distinct s.product_id, p.product_name
from Sales s
left join Product p
on s.product_id = p.product_id
where s.product_id not in (select product_id from cte);
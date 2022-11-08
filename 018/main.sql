-- https://leetcode.com/problems/group-sold-products-by-the-date/

-- 了解如何使用 group_concat 將多個值合成陣列到一個欄位
-- 了解 group by 的總和量可以用 distinct 作為加總的條件

select sell_date, count(distinct product) num_sold, group_concat(distinct product) products
from Activities
group by sell_date;
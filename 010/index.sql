-- https://leetcode.com/problems/sales-person/
-- 這題太經典了，可以將基本的 SQL left join, 差集, subquery 都運用上

select s.name
from SalesPerson s
left join (
    select o.sales_id
    from Orders o
    left join Company c
    on o.com_id = c.com_id
    where c.name = 'RED'
) oc
on s.sales_id = oc.sales_id
where oc.sales_id is null;
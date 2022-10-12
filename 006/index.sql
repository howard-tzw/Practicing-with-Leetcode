-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/submissions/
-- group by + order by 的組合技
-- count(*) 可以抓出 group by 的組合數量！
select customer_number
from orders
group by customer_number
order by count(*) desc
limit 1;
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

-- 自己的解法
-- 快很多 Beats 86.33% 1183ms
select v.customer_id, count(*) count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id;

-- 別人的解法，學習使用 in 和 not in
-- 比較慢 Beats 7.48% 2707ms
select customer_id, count(visit_id) count_no_trans
from Visits v
where v.visit_id not in (select visit_id from Transactions)
group by customer_id;

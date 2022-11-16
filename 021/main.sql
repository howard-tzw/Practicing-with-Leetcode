-- https://leetcode.com/problems/bank-account-summary-ii/
-- 基本題，使用 left join + group by

select name, sum(t.amount) balance
from Users u
left join Transactions t
on u.account = t.account
group by t.account
having balance > 10000
-- https://leetcode.com/problems/swap-salary/

-- 瞭解如何使用 case when then end

update salary
set sex =
case
when sex="m" then "f"
when sex="f" then "m"
end;
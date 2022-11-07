-- https://leetcode.com/problems/top-travellers/
-- 好題目！把最基本的 SQL 語法都用上了

select u.name, if(r.travelled_distance is null, 0, r.travelled_distance) travelled_distance
from Users u
left join (
    select sum(distance) travelled_distance, ri.user_id
    from Rides ri
    group by ri.user_id
) r
on u.id = r.user_id
order by r.travelled_distance desc, u.name asc;
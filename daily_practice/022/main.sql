-- https://leetcode.com/problems/fix-names-in-a-table/

-- learn to write 'concat, upper, left, lower, substring, length'

select 
user_id, 
concat(upper(left(u.name, 1)), lower(substring(u.name, 2, length(u.name)))) name
from Users u
order by user_id

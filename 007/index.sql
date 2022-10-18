-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
-- group by 可以用兩個以上的欄位，符合所有欄位值皆相同資料才會被分為一組
-- 同上一題要運用 count(*)

select actor_id, director_id 
from ActorDirector
group by actor_id, director_id
having count(*) >= 3;
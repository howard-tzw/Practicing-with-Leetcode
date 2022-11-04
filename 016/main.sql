-- https://leetcode.com/problems/reformat-department-table/

-- 了解如何將欄位的值轉成欄位的名稱
-- mssql 有 pivot 語法，但 mysql 和 pg 都沒有，所以要會使用 case when...then...else...end 以及 group by

select id,
    sum(case when month = 'jan' then revenue else null end) Jan_Revenue,
    sum(case when month = 'feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'may' then revenue else null end) as May_Revenue,
	sum(case when month = 'jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from Department
group by id
order by id;

-- pivot 參考 
-- https://littlehorseboy.github.io/2020/05/31/2020-t-sql-pivot/#%E5%BB%BA%E7%AB%8B-TempTable-%E7%9A%84%E7%A4%BA%E7%AF%84%E8%B3%87%E6%96%99
-- https://leetcode.com/problems/daily-leads-and-partners/

-- learn count distinct plus group by

select date_id, make_name, count(DISTINCT lead_id) unique_leads, count(DISTINCT partner_id) unique_partners
from DailySales
group by date_id, make_name;
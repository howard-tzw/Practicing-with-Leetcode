-- https://leetcode.com/problems/patients-with-a-condition/

-- 學習使用 like

select patient_id, patient_name, conditions
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%';
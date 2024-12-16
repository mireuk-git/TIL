# https://leetcode.com/problems/employees-whose-manager-left-the-company/submissions/1479793988/

select employee_id 
from Employees
where manager_id is not null 
and manager_id not in (select employee_id from Employees)
and salary < 30000
order by employee_id
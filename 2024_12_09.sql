# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/

select e1.employee_id, e1.name, count(e2.name) as reports_count, round(avg(e2.age)) as average_age
from Employees e1 join Employees e2
where e2.reports_to = e1.employee_id
group by e1.employee_id
order by employee_id

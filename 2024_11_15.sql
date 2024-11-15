#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/1453151986/

select U.unique_id, E.name
from Employees E left join EmployeeUNI U
on E.id = U.id
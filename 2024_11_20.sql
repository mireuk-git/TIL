# https://leetcode.com/problems/employee-bonus/solutions/5302949/mysql-left-join-beats-98/

select E.name, B.bonus
from Employee E left join Bonus B on E.empId=B.empId
where B.bonus is null or B.bonus<1000
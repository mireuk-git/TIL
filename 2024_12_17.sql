# https://leetcode.com/problems/exchange-seats/

select id, case
when id%2=0 then lag(student) over(order by id)
else coalesce(lead(student) over(order by id), student)
end as student
from seat
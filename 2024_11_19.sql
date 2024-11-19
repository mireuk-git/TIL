# https://leetcode.com/problems/average-time-of-process-per-machine/description/

select A1.machine_id, round(avg(A2.timestamp-A1.timestamp),3) as processing_time
from 
(select * from Activity where activity_type='start') A1 join
(select * from Activity where activity_type='end') A2
on A1.machine_id = A2.machine_id and A1.process_id = A2.process_id
group by A1.machine_id
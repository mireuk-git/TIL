# https://leetcode.com/problems/students-and-examinations/submissions/1458721621/

select s.student_id, s.student_name, sub.subject_name, count(e.student_id) as attended_exams
from (students s, subjects sub)
left join examinations e on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, sub.subject_name
order by s.student_id, sub.subject_name
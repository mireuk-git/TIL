# https://leetcode.com/problems/movie-rating/

(select u.name as results
from users u join MovieRating r on r.user_id = u.user_id
group by r.user_id
order by count(*) desc, name
limit 1)
union all
(select m.title as results
from movies m join movierating r on m.movie_id = r.movie_id
where r.created_at >= '2020-02-01' and r.created_at<'2020-03-01'
group by m.movie_id
order by avg(r.rating) desc, title
limit 1)
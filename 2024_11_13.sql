#https://leetcode.com/problems/article-views-i/

select author_id as id from Views
where author_id = viewer_id
group by author_id, viewer_id
order by id
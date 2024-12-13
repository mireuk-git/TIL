# https://leetcode.com/problems/product-price-at-a-given-date/

with latest as (
    select product_id, max(change_date) as latest_date
    from products
    where change_date<='2019-08-16'
    group by product_id
)
(select p.product_id, p.new_price as price
from products p join latest l
where p.product_id = l.product_id and p.change_date = l.latest_date)
union
(select product_id, 10 as price
from products where product_id not in (select product_id from latest))
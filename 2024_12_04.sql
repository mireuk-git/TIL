# https://leetcode.com/problems/product-sales-analysis-iii/description/

with f as (
    select product_id, min(year) as year
    from Sales
    group by product_id
)

select s.product_id, s.year as first_year, s.quantity, s.price
from Sales s join f
on (s.product_id,s.year) = (f.product_id,f.year)
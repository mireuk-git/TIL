# https://docs.google.com/forms/d/e/1FAIpQLSdYoMIST274z6oAQrCiui6bdqNtuWNt7j5aMnacg2_Pj8v5VQ/viewform

select *,
case
when x+y-z>0 and x+z-y>0 and y+z-x>0 then "Yes"
else "No"
end as triangle
from Triangle

# https://www.acmicpc.net/problem/13959
# 13959

d=int(input())
r=int(input())
t=int(input())

r_sum=0
r_curr=4
t_sum=0
t_curr=4-d

while r_sum<r:
    r_sum+=r_curr
    r_curr+=1
    if t_curr>=3: t_sum+=t_curr
    t_curr+=1
    if t_sum>t:
        if t_sum-t == r-r_sum:
            break
print(r-r_sum)

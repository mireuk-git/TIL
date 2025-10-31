# https://www.acmicpc.net/problem/15131
# 15131

n = int(input())
power_to_segments = {0:0,2:1,3:7,4:4}
sum = n//3*7
n%=3
if n==1:
    sum-=7
    n+=3
sum+=power_to_segments[n]
print(sum)
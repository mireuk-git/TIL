# https://www.acmicpc.net/problem/17252
# 17252

n = int(input())
s=n
for i in range(19,-1,-1):
    if 3**i<=s:
        s-=3**i
if n!=0 and s==0: print("YES")
else: print("NO")
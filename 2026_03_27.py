# https://www.acmicpc.net/problem/15236

n=int(input())
spot=0
c=1
for i in range(n+1):
    spot+=c*i
    if (i%2==1): c+=1
c-=1
for i in range(n+1,2*n+1):
    spot+=c*i
    if (i%2==0): c-=1
print(spot)
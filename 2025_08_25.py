# https://www.acmicpc.net/problem/26090
# 26090

n=int(input())
a=list(map(int,input().split()))

s=max(sum(a),n)
eratos=[True for _ in range(s+1)]
eratos[0],eratos[1]=False,False
for i in range(2,s+1):
    if eratos[i]: 
        tmp=i+i
        while tmp<=s:
            eratos[tmp]=False
            tmp+=i

count=0
l=2
while l<=n:
    if eratos[l]:
        for i in range(n-l+1):
            if eratos[sum(a[i:i+l])]:
                count+=1
    l+=1
print(count)

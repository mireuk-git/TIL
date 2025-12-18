# https://www.acmicpc.net/problem/14911
# 14911

l=list(map(int,input().split()))
n=int(input())
l.sort()

left,right = 0,len(l)-1
results=[]
results_set=set()
while left<right:
    sum=l[left]+l[right]
    if sum==n and (l[left],l[right]) not in results_set:
        results.append((l[left],l[right]))
        results_set.add((l[left],l[right]))
        left+=1
        right-=1
    elif sum<n: left+=1
    else: right-=1

for i in results:
    print(f"{i[0]} {i[1]}")
print(len(results))
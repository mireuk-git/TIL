# https://www.acmicpc.net/problem/14410
# 14410

n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)

max_diff=[100,0]
left=0
total=sum(l)
for i in range(n):
    left+=l[i]
    a=(i+1)*100/n
    b=left*100/total
    if max_diff[1]-max_diff[0] < b-a:
        max_diff=[a,b]
    else: break
print(max_diff[0],max_diff[1])
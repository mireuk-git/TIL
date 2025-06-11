# https://www.acmicpc.net/problem/30266
# 30266
'''
import sys
input=sys.stdin.readline

k=int(input().strip())
for set_num in range(1,1+k):
    n=int(input().strip())
    broadcast=set(input().strip())
    c=0
    for _ in range(n):
        consumed=input().strip()
        for i in broadcast:
            if i in consumed:
                c+=1
                break
    print(f"Data Set {set_num}:\n{c}\n")
'''
# https://www.acmicpc.net/problem/28323
# 28323
'''
def dfs(a,b,i):
    if i>=len(a):
        flag=True
        if len(b)==1 and b[0]%2==0: flag=False
        for i in range(len(b)-1):
            if (b[i]+b[i+1])%2==0:
                flag=False
                break
        if flag and b: return len(b)
        else: return -1
    else:
        c1=dfs(a,b,i+1)
        b+=(a[i],)
        c2=dfs(a,b,i+1)
        return max(c1,c2)

n=int(input())
a=list(map(int,input().split()))
print(dfs(a,(),0))
'''
'''
n=int(input())
a=list(map(int,input().split()))
i=0
while i < len(a)-1:
    if (a[i]+a[i+1])%2==0:
        a.pop(i)
    else: i+=1
print(len(a))
'''
n=int(input())
arr=list(map(int,input().split()))
idx=0
count=1
for i in range(1,n):
    if (arr[idx]+arr[i])%2:
        count+=1
        idx=i
print(count)

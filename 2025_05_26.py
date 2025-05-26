# https://www.acmicpc.net/problem/11636
# 11636
'''
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    c=0
    for i in range(1,len(l)):
        if l[i]>l[i-1]*2:
            c+=l[i]-l[i-1]*2
    print(c)
    '''
# https://www.acmicpc.net/problem/16847
# 16847
'''
K=int(input())
for _ in range(K):
    n,k=map(int,input().split())
    s=[]
    c=0
    for i in range(n+1):
        s.append(input())
    for i in range(k):
        c+=1
        for j in range(1,n+1):
            if s[0][i]==s[j][i]:
                c-=1
                break
    print(f"Data Set {_+1}:\n{c}/{k}\n")
'''
# https://www.acmicpc.net/problem/10570
# 10570

from collections import Counter
n=int(input())
for _ in range(n):
    v=int(input())
    s=[]
    for i in range(v):
        s.append(int(input()))
    s=Counter(s)
    m,M=0,0
    for i in sorted(s.keys()):
        if m<s[i]:
            m,M=s[i],i
    print(M)

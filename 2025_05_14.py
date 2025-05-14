# https://www.acmicpc.net/problem/12166
# 12166
'''
import sys
input=sys.stdin.readline

t=int(input().strip())
for _ in range(1,t+1):
    s_max,S=input().strip().split()
    s_max=int(s_max)
    s=0
    c=0
    for k in range(s_max+1):
        if s>=k: s+=int(S[k])
        else: 
            c+=k-s
            s=k+int(S[k])
    print(f"Case #{_}:",c)
'''
# https://www.acmicpc.net/problem/23544
# 23544

n=int(input())
hippo=set()
for _ in range(n):
    hippo.add(input())
print(n-len(hippo))
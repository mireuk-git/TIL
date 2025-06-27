# https://www.acmicpc.net/problem/33540
# 33540

n=int(input())
m={}
for i in range(n):
    name,score=input().split()
    if name in m.keys():
        m[name]+=int(score)
    else: 
        m[name]=int(score)
for i in sorted(m.keys()):
    print(i,m[i])

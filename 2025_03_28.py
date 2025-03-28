# https://www.acmicpc.net/problem/14375
# 14375

t=int(input())
for _ in range(1,t+1):
    S=input()
    r=S[0]
    for i in range(1,len(S)):
        if S[i]<r[0]:
            r+=S[i]
        else: 
            r=S[i]+r
    print(f"Case #{_}:",r)
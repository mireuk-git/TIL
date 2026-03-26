# https://www.acmicpc.net/problem/10419

t=int(input())
l=[0]
for test_case in range(t):
    d=int(input())
    while l[-1]<d: l.append(len(l)*(len(l)+1))
    for i in range(len(l)-1,-1,-1):
        if l[i]<=d:
            print(i)
            break

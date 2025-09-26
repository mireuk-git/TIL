# https://www.acmicpc.net/problem/12185
# 12185

t=int(input())
for test_case in range(1,1+t):
    if test_case>1: input()
    n=int(input())
    l=list(map(int,input().split()))
    bus=[]
    for i in range(n):
        bus.append([l[i*2],l[i*2+1]])
    p=int(input())
    r=f"Case #{test_case}: "
    for _ in range(p):
        count=0
        c=int(input())
        for i in range(n):
            if c>=bus[i][0] and c<=bus[i][1]:
                count+=1
        r+=str(count)+" "
    print(r)


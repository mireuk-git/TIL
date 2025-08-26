# https://www.acmicpc.net/problem/14791
# 14791

t=int(input())
for test_case in range(1,t+1):
    n=int(input())
    l=list(map(int,list(str(n))))
    flag=False
    i=1
    while i < len(l):
        if flag:
            l[i]=9
        elif l[i-1]>l[i]: 
            while i>0 and l[i-1]>=l[i]: i-=1
            l[i]-=1
            flag=True
        i+=1
    s=''
    for i in l: s+=str(i)
    print(f"Case #{test_case}:",int(s))
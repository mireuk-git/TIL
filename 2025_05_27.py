# https://www.acmicpc.net/problem/23717
# 23717
'''
t=int(input())
c={"r":['R','O','P','A'],'y':['Y','O','G','A'],'b':['B','G','P','A']}
for _ in range(t):
    n=int(input())
    s=input()

    count=0
    for p in ['r','b','y']:
        i=0
        while i<n:
            while i<n and s[i] not in c[p]: i+=1
            while i<n and s[i] in c[p]: i+=1
            count+=1
        if s[-1] not in c[p]: count-=1
    print(f"Case #{_+1}:",count)
'''
# https://www.acmicpc.net/problem/3186
# 3186

k,l,n=map(int,input().split())
s=input()+'0'*(k+l)
i=0
while i<n:
    while i<n and s[i]=='0': i+=1
    if s[i:i+k]=='1'*k: 
        i+=k
        while s[i:i+l]!='0'*l:
            i+=1
        i+=l
        print(i)
    else: i+=1

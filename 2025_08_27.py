# https://www.acmicpc.net/problem/23971
# 23971
'''
h,w,n,m=map(int,input().split())
H=(h+n)//(n+1)
W=(w+m)//(m+1)
print(H*W)
'''
# https://www.acmicpc.net/problem/31832
# 31832

n=int(input())
flag=False
r=''
for i in range(n):
    s=input()
    if flag: continue
    if len(s)>10: continue
    count=[0,0]
    number=True
    for j in range(len(s)):
        if ord(s[j])>=97 and ord(s[j])<=122:
            count[0]+=1
            number=False
        elif ord(s[j])>=65 and ord(s[j])<=90:
            count[1]+=1
            number=False
        elif ord(s[j])==45: number=False
    
    if not number and count[0]>=count[1]: 
        r=s
        flag=True
print(r)
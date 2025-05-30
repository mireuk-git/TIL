# https://www.acmicpc.net/problem/18706
# 18706

t=int(input())
for case_num in range(1,t+1):
    c,p=map(int,input().split())
    coffee={}
    fee={}
    for i in range(c):
        n,s,m,l=input().split()
        s,m,l=map(int,(s,m,l))
        coffee[n]={"small":s,"medium":m,"large":l}

    for i in range(p):
        x,y,z=input().split()
        if not x in fee.keys():
            fee[x]=0
        fee[x]+=coffee[z][y]
    
    for i in fee.keys():
        fee[i]+=100//len(fee.keys())
        if fee[i]%5==1: fee[i]-=1
        elif fee[i]%5==4: fee[i]+=1
        print(i,fee[i])

# https://www.acmicpc.net/problem/32046

n=int(input())
while n>0:
    a=list(map(int,input().split()))
    sum=0
    for i in range(n):
        sum+=a[i]
        if sum>300:
            sum-=a[i]
    print(sum)
    n=int(input())
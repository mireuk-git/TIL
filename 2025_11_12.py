# https://www.acmicpc.net/problem/1427
# python

n=int(input())
separated = []
while n>0:
    separated.append(n%10)
    n//=10
separated.sort(reverse=True)
for i in separated:
    print(i,end='')
# https://www.acmicpc.net/problem/4635
# 4635
'''
n=int(input())
while n!=-1:
    distance=0
    prev_t=0
    for i in range(n):
        s,t=map(int,input().split())
        distance+=s*(t-prev_t)
        prev_t=t
    print(f"{distance} miles")
    n=int(input())
'''
# https://www.acmicpc.net/problem/7857
# 7857

n=int(input())
a=[input()]
byte=len(a[0])
for i in range(1,n):
    a.append(input())
    j=0
    while j<min(len(a[i-1]),len(a[i])) and a[i][j]==a[i-1][j]: 
        j+=1
    byte+=len(a[i])-j+1
print(byte)

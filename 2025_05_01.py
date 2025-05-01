# https://www.acmicpc.net/problem/4992
# 4992
'''
while True:
    n,r=map(int,input().split())
    if n==0 and r==0: break
    deck={i:n-i for i in range(n)}

    for _ in range(r):
        p,c=map(int,input().split())
        tmp=[deck[i] for i in range(p-1)]
        for i in range(c): deck[i]=deck[p-1+i]
        for i in range(p-1): deck[c+i]=tmp[i]
    print(deck[0])
'''
# https://www.acmicpc.net/problem/1788
# 1788

f=[]

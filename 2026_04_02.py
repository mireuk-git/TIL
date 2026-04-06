# https://www.acmicpc.net/problem/13877
'''
t = int(input())
for testcase in range(1,1+t):
    k,n = input().split()
    o=0
    for c in n:
        if c>'7':
            o=0
            break
        o = o*8+int(c)
    h=0
    for c in n: h = h*16+int(c)
    print(k, o, n, h)
'''

t=int(input())
for testcase in range(t):
    k,n=input().split()
    if any(c in '89' for c in n):
        o = 0
    else: 
        o = int(n,8)
    
    h = int(n,16)
    print(k, o, n, h)
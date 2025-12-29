# https://www.acmicpc.net/problem/22193
# 22193
'''
n,m=map(int,input().split())
a=int(input())
b=int(input())
print(a*b)
'''
# https://www.acmicpc.net/problem/2998
# 2998
'''
b=input()
b='0'*(3-len(b)%3)+b
o=''
for i in range(0,len(b),3):
    t=0
    for j in range(3):
        t*=2
        t+=int(b[i+j])
    o+=str(t)
print(o.lstrip('0'))
'''
b=input()
d=int(b,2)
o=format(d,'o')
print(o)
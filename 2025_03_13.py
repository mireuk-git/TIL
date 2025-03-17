# https://www.acmicpc.net/problem/20004
# 20004
'''
a=int(input())
for n in range(1,a+1):
    if (30)%(n+1)==0: 
            print(n)
'''

# https://www.acmicpc.net/problem/27919
# 27919
from math import ceil
l=[0,0]
v=input()
l[0]=v.count("U")+v.count("C")
l[1]=v.count("D")+v.count("P")
if l[0]>0 and l[0]>ceil(l[1]/2): print("U",end='')
if l[1]>0: print("DP",end='')
if len(v)==0: print("C")
print('')

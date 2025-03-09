# https://www.acmicpc.net/problem/6764
# 6764
'''
l=[]
for i in range(4): l.append(int(input()))

rising=True
diving=True

for i in range(1,4):
    if rising and l[i]<=l[i-1]: rising=False
    if diving and l[i]>=l[i-1]: diving=False

if rising: print("Fish Rising")
elif diving: print("Fish Diving")
elif len(set(l))==1: print("Fish At Constant Depth")
else: print("No Fish")
'''

# https://www.acmicpc.net/problem/2097
# 2097

from math import sqrt
n=int(input())
w=int(sqrt(n))
h=w
while h*w<n: h+=1
h-=1
w-=1
print("h:",h)
print("w:",w)
print((h+w)*2)



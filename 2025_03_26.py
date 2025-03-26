# https://www.acmicpc.net/problem/20254
'''
Ur,Tr,Uo,To=map(int,input().split())
print(56*Ur+24*Tr+14*Uo+6*To)
'''
# https://www.acmicpc.net/problem/33643

n=int(input())
l=["keys","phone","wallet"]
for i in range(n):
    t=input()
    if t in l: l.remove(t)
if l: 
    for i in l: print(i)
else: print("ready")
# https://www.acmicpc.net/problem/32326
# 32326
'''
r=int(input())
g=int(input())
b=int(input())
c=r*3+g*4+b*5
print(c)
'''

# https://www.acmicpc.net/problem/18129
# 

s,k=input().split()
k=int(k)
s=s.lower()
index=0
left=0
r=''
used=set()
while index<len(s):
    while index<len(s) and s[left]==s[index]: index+=1
    if s[left] not in used: 
        if index-left>=k: r+='1'
        else: r+='0'
    used.add(s[left])
    left=index
    
print(r)
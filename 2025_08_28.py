# https://www.acmicpc.net/problem/30458
# 30458
'''
from collections import Counter
n=int(input())
s=input()
c=Counter(s)
result="Yes"
for i in c.keys():
    if c[i]%2 and i!=s[n//2]: result="No"
print(result)
'''
# https://www.acmicpc.net/problem/12981
# 12981
'''
r,g,b=map(int,input().split())
count=0
count+=r//3
r%=3
count+=g//3
g%=3
count+=b//3
b%=3
if [r,g,b].count(0)==2: count+=1
else: count+=max(r,g,b)
print(count)
'''
# https://www.acmicpc.net/problem/4368
# 4368

import sys
feed=sys.stdin.readline().strip()
dictionary=dict()
while feed!='':
    value,key=feed.split()
    dictionary[key]=value
    feed=sys.stdin.readline().strip()

words=sys.stdin.readlines()
for i in words:
    word=i.strip()
    if word in dictionary.keys():
        print(dictionary[word])
    else:
        print("eh")
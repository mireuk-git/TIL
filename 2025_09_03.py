# https://www.acmicpc.net/problem/16170
# 16170
'''
from datetime import datetime, timedelta
now=datetime.now()
UTC=now-timedelta(hours=9)
print(UTC.year)
print(UTC.month)
print(UTC.day)
'''
# https://www.acmicpc.net/problem/8595
# 8595

n=int(input())
feed=input()
left=-1
s=0
for i in range(n):
    if ord(feed[i])>=48 and ord(feed[i])<=57:
        if left<0:
            left=i
    elif left>=0:
        s+=int(feed[left:i])
        left=-1
if ord(feed[i])>=48 and ord(feed[i])<=57:
    s+=int(feed[left:i+1])
print(s)
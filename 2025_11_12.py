# https://www.acmicpc.net/problem/1427
# 1427
'''
n=int(input())
separated = []
while n>0:
    separated.append(n%10)
    n//=10
separated.sort(reverse=True)
for i in separated:
    print(i,end='')
'''
# https://www.acmicpc.net/problem/6119
# 6119

import sys
from collections import deque
input = sys.stdin.readline 

s=int(input().strip())
queue=deque([])
i=1
for _ in range(s):
    op,remains=input().strip().split(" ",1)
    if op == 'A':
        if remains == 'L': queue.appendleft(i)
        elif remains == 'R': queue.append(i)
        i+=1
    elif op == 'D':
        direction,count=remains.split()
        if direction == 'L':
            for j in range(int(count)):
                queue.popleft()
        elif direction == 'R':
            for j in range(int(count)):
                queue.pop();
for i in queue:
    print(i)
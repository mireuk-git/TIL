# https://school.programmers.co.kr/learn/courses/30/lessons/154538
'''
from collections import deque

def solution(x,y,n):
    if x==y: return
    queue = deque([(x,0)])
    while queue:
        x,s = queue.popleft()
        s+=1

        r = x+n
        if r==y: return s
        elif x<y: queue.append(r,s)

        r = x*2
        if r==y: return s
        elif x<y: queue.append(r,s)

        r = x*3
        if r==y: return s
        elif x<y: queue.append(r,s)

    return -1
'''
from collections import deque
def solution(x,y,n):
    queue = deque([(y,0)])
    while queue:
        y,s = queue.popleft()
        if x==y: return s
        elif x>y: continue

        if y%3==0: queue.append((y//3,s+1))
        if y%2==0: queue.append((y//2,s+1))
        queue.append((y-n,s+1))
    return -1
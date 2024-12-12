# https://school.programmers.co.kr/learn/courses/30/lessons/118667

'''
def solution(queue1, queue2):
    q1,q2=sum(queue1),sum(queue2)
    for i in range(len(queue1)*3):
        if q1>q2:
            q1-=queue1[0]
            q2+=queue1[0]
            queue2.append(queue1.pop(0))
        elif q1<q2:
            q1+=queue2[0]
            q2-=queue2[0]
            queue1.append(queue2.pop(0))
        else: return i
    return -1
'''
from collections import deque
def solution(queue1, queue2):
    queue1,queue2=deque(queue1),deque(queue2)
    q1,q2=sum(queue1),sum(queue2)
    for i in range(len(queue1)*3):
        if q1>q2:
            q1-=queue1[0]
            q2+=queue1[0]
            queue2.append(queue1.popleft())
        elif q1<q2:
            q1+=queue2[0]
            q2-=queue2[0]
            queue1.append(queue2.popleft())
        else: return i
    return -1
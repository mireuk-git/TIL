# https://school.programmers.co.kr/learn/courses/30/lessons/140107

from math import sqrt

def solution(k,d):
    count=0
    for y in range(0,d+1,k):
        count+=int(sqrt(d**2-y**2))//k+1
    return count

print(solution(1,5))

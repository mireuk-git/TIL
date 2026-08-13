# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k,tangerine):
    counter = Counter(tangerine)
    value = sorted(counter.values(),reverse=True)
    i=0
    while k>0:
        k-=value[i]
        i+=1
    return i
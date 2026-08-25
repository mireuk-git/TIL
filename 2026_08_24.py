# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

def solution(orders,course):
    l = []
    for c in course:
        # Combination(o,c)
        counter = Counter()
        for o in orders:
            o = sorted(o)
            counter.update(combinations(o,c))
        # 최빈값
        m = 0
        for i in counter.keys():
            if counter[i]>m:
                m = counter[i]
                t = [i]
            elif counter[i]==m:
                t.append(i)
        # 리스트에 추가
        if m>=2:
            for mi in t:
                # String화
                s = ''
                for i in mi: s+=i
                l.append(s)
    l = sorted(list(set(l)))
    return l

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
r=solution(orders,course)
print(r)
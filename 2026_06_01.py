# https://school.programmers.co.kr/learn/courses/30/lessons/388352

from itertools import combinations

def solution(n,q,ans):
    candidates = list(combinations(range(1,n+1),5))
    for i in range(len(q)):
        new_candidates=[]
        for c in candidates:
            count=0
            for e in q[i]:
                if e in c: count+=1
            if count==ans[i]: new_candidates.append(c)
        candidates=new_candidates
    return len(candidates)


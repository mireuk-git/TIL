# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import Counter
def solution(weights):
    ratio = [(2,3),(1,2),(3,4)]
    counter = Counter(weights)

    answer=0
    for k in counter.keys():
        # calculate target
        for r in ratio:
            if k%r[0]>0: continue
            target = k*r[1]//r[0]
            answer+=counter[k]*counter[target]
        # 1:1ratio nCr
        answer += counter[k]*(counter[k]-1)//2
    return answer
solution([100,150])
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from math import ceil

def solution(progresses, speeds):
    iter = 0
    result = []
    while (iter<len(progresses)):
        days = ceil((100-progresses[iter])/speeds[iter])
        cnt = 1
        iter += 1
        while(iter<len(progresses) and speeds[iter]*days+progresses[iter]>=100):
            cnt += 1
            iter += 1
        result.append(cnt)
    return result

progresses = [99,1]
speeds = [100, 125]

print(solution(progresses,speeds))
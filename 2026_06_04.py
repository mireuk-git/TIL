# https://school.programmers.co.kr/learn/courses/30/lessons/340212
'''
def solution(diffs, times, limit):
    high = 100000
    low = 1
    length = len(diffs)
    while(True):
        level=(high+low)//2
        t=0
        for i in range(length):
            if (diffs[i]<=level): t+=times[i]
            else: 
                if i<=0: times[0]*(diffs[i]-level+1)
                else: t+=((times[i-1]+times[i])*(diffs[i]-level)+times[i])
        if t<=limit: high = level
        else: low = level
        if high-low<=1:
            return high
'''

def tpp(diff, time_cur, time_prev, level):
    if level<diff:
        return (diff-level)*(time_cur+time_prev)+time_cur
    else:
        return time_cur


def solution(diffs, times, limit):
    high = 100000
    low = 0
    while True:
        level = (high+low)//2
        t=tpp(diffs[i], times[0], 0, level)
        for i in range(len(diffs)):
            t+=tpp(diffs[i],times[i],times[i-1],level)
        if tpp<=limit: high = level
        else: low = level
        if high-low<=1: return high

print(solution([1,5,3],[2,4,7],30))



# https://school.programmers.co.kr/learn/courses/30/lessons/142085
'''
def solution(n,k,enemy):
    i=0
    tmp=[]
    for i in range(len(enemy)):
        tmp.append(enemy[i])
        # use cheat
        if n<enemy[i]:
            if k>0:
                # find the optimal timing
                tmp.sort()
                n+=tmp.pop()
                k-=1
            else: return i
        # progress round
        n-=enemy[i]
        print(tmp, n)
    return i+1
'''

import heapq

def solution(n, k, enemy):
    heap = []

    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        n -= e

        if n < 0:
            if k == 0:
                return i
            k -= 1
            n += -heapq.heappop(heap)

    return len(enemy)

enemy = [4,2,4,5,3,3,1]	
print(solution(7,3,enemy))
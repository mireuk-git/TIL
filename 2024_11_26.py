# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    #모든 경우의 수
    dungeons_per = []
    for i in permutations(dungeons,len(dungeons)):
        dungeons_per.append(list(i))
    #검증 단계
    p=[]
    for i in dungeons_per:
        s,count=k,0
        for j in i:
            if s>=j[0]:
                s-=j[1]
                count+=1
            elif s<j[0]: break
        p.append(count)
    answer=max(p)
    return answer
            
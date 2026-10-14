# https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    n = len(cards)
    group = [0]*n #group[i]: 상자i의 소속 그룹
    t = 1
    count=[0,0] #count[t]: 그룹t의 원소 개수
    # 그룹화
    # 모든 상자에 대해 dfs
    for i in range(n):
        while group[i]==0:
            group[i]=t
            count[t]+=1
            i=cards[i]-1
            if group[i]!=0: 
                t+=1
                count.append(0)
    # 곱의 최대값
    count.sort(reverse=True)
    # 그룹이 하나밖에 없으면 더미 데이터 0이 섞여 리턴값이 0이 된다
    return count[0]*count[1] 

print(solution([8,6,3,7,2,5,1,4]))
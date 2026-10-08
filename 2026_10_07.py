# https://school.programmers.co.kr/learn/courses/30/lessons/150369
'''
def solution(cap,n,deliveries,pickups):
    weight = 0
    turn = n-1 #greedy: 먼거리부터 배달
    distance = 0
    while turn>0:
        while deliveries[turn]==pickups[turn]==0:
            turn-=1
        #택배배달
        i=turn
        while weight>0:
            deliveries[i]-=1
            if deliveries[i]==0: i-=1
        #택배픽업
        i=turn
        while weight<n:
            pickups[i]-=1
            if pickups[i]==0: i-=1
        distance+=turn+1
    return distance
'''
def solution(cap,n,deliveries,pickups):
    distance = 0
    
    di = n-1 #delivery remain index
    pi = n-1 #pickup remain index

    while di>=0 or pi>=0:
        while di >= 0 and deliveries[di]==0: di-=1
        while pi >= 0 and pickups[pi]==0: pi-=1
        furthest = max(di,pi)
        if furthest<0: break
        distance+=(furthest+1)*2

        capacity = cap
        while di>=0 and capacity>0:
            use = min(deliveries[di],capacity)
            deliveries[di] -= use
            capacity -= use
            if deliveries[di]==0: di-=1

        capacity = cap
        while pi>=0 and capacity>0:
            use = min(pickups[pi],capacity)
            pickups[pi]-=use
            capacity-=use
            if pickups[pi]==0: pi-=1
    return distance

deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
print(solution(4,5,deliveries,pickups))
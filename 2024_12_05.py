# https://school.programmers.co.kr/learn/courses/30/lessons/42583

'''
def solution(bridge_length, weight, truck_weights):
    bridge=[]
    for truck in truck_weights:
        on_bridge=bridge[-1:-(bridge_length):-1]
        while sum(on_bridge)+truck>weight:
            bridge.append(0)
            on_bridge=bridge[-1:-(bridge_length):-1]
        bridge.append(truck)
    return len(bridge)+bridge_length
'''

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    bridge_weight=0
    answer=0
    while truck_weights :
        answer +=1
        bridge_weight-=bridge[0]
        bridge.pop(0)
        bridge.append(0)
        if bridge_weight + truck_weights[0] <= weight :
            bridge[-1] = truck_weights.pop(0)
            bridge_weight+=bridge[-1]
    return answer + bridge_length
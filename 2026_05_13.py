# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    if wallet[0]>wallet[1]: wallet=wallet[::-1]
    if bill[0]>bill[1]: bill=bill[::-1]
    answer=0

    while wallet[0]<bill[0] or wallet[1]<bill[1]:
        bill[1]//=2
        answer+=1
        if bill[0]>bill[1]: bill=bill[::-1]
    return answer


wallet=[50,50]
bill=[100,241]
print(solution(wallet,bill))
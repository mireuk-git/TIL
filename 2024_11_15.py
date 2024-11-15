def solution(n):
    answer=[1,2,3]
    while len(answer)<n:
        answer.append(answer[-1]+answer[-2])
    return answer[n-1]%1234567
def solution(lottos, win_nums):
    answer = [7,7]
    for i in lottos:
        if i in win_nums:
            answer[0]-=1
            answer[1]-=1
        if i == 0:
            answer[0]-=1
    for i in range(len(answer)):
        if answer[i]==7: answer[i]-=1
    return answer
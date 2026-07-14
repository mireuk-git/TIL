# https://school.programmers.co.kr/learn/courses/30/lessons/154539
'''
def solution(numbers):
    answer=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]<numbers[j]:
                answer.append(numbers[j])
                break
        if len(answer)<=i:
            answer.append(-1)
    return answer

print(solution([9,1,5,3,6,2]))
'''


def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for idx,num in enumerate(numbers):
        while stack and numbers[stack[-1]]<num:
            answer[stack.pop()]=num
        stack.append(idx)
    return answer
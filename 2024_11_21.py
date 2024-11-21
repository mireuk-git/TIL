# https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            answer[i].append(0)
            for k in range(len(arr2)):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer
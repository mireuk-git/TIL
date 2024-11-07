# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0 for i in id_list]
    reported={i:set() for _,i in enumerate(id_list)}
    for i in report:
        init, vic = i.split()
        reported[vic].add(init)
    for i in id_list:
        if len(reported[i])>=k:
            for j in range(len(id_list)):
                if id_list[j] in reported[i]: answer[j]+=1
    return answer
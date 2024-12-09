# https://school.programmers.co.kr/learn/courses/30/lessons/131704

'''
def solution(order):
    answer=0
    main,sub = 1,0
    for i in range(len(order)):
        if main<order[i]:
            main=order[i]+1
            sub=order[i]-1
            answer+=1
        elif main>order[i]:
            if sub == order[i]:
                answer+=1
                sub-=1
                while sub in order[:i]: sub-=1
            else: return answer
        else: #main==order[i]
            answer+=1
            main+=1
    return answer
'''
def solution(order):
    answer=0
    main,sub = 1,[]
    for i in range(len(order)):
        if main<order[i]:
            for j in range(main,order[i]):
                sub.append(j)
            main=order[i]+1
            answer+=1
        elif main>order[i]:
            if sub[-1] == order[i]:
                answer+=1
                sub.pop(-1)
            else: return answer
        else: #main==order[i]
            answer+=1
            main+=1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    for p in plans: #시간 int화
        h,m = map(int,p[1].split(":"))
        p[1] = h*60+m
        p[2] = int(p[2])
    plans.sort(key = lambda x: x[1])
    t = plans[0][1] #현재 시간
    stack = [] #하다 만 과제
    finished = [] #끝난 과제

    for i in range(len(plans)):
        while stack and t<plans[i][1]: #하다 만 과제가 있다면, 다음 과제 시작 전이라면
            w = stack.pop()
            if t+w[2]>plans[i][1]: #다음 과제 전에 안끝내면
                w[2] -= plans[i][1]-t
                t=plans[i][1]
                stack.append(w)
            else: #끝내면
                t+=w[2]
                finished.append(w[0])

        t=plans[i][1] #과제 시작
        if i<len(plans)-1 and t+plans[i][2]>plans[i+1][1]: #다음과제 전에 안끝난다면
            plans[i][2] -= plans[i+1][1]-t
            t=plans[i+1][1]
            stack.append(plans[i])
        else: #끝내면
            t+=plans[i][2]
            finished.append(plans[i][0])
    #잔반처리
    while stack:
        w = stack.pop()
        finished.append(w[0])
    return finished

plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
print(solution(plans))
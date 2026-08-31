# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    t = []
    num = ""
    for c in s[1:-1]:
        if c == '{':
            tmp=[]
            open = True
        elif c.isdigit(): num+=c
        elif c == ',' and open:
            tmp.append(int(num))
            num = ""
        elif c == "}":
            if num: 
                tmp.append(int(num))
                num = ""
            t.append(tmp)
            open = False

    t.sort(key=lambda x: len(x))

    result = []
    for i in t:
        e = (set(i)-set(result)).pop()
        result.append(e)
    return result
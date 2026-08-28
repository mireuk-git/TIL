# https://school.programmers.co.kr/learn/courses/30/lessons/67257

def solution(expression):
    operator = [] #연산해야 할 연산자
    for o in ["+","*","-"]:
        if o in expression: 
            operator.append(o)
    #expression list로 쪼개기
    xps = [] #쪼개진 expression
    num = ""
    for c in expression:
        if c.isdigit(): num+=c
        else: 
            if num: 
                xps.append(int(num))
                num=""
            xps.append(c)
    if num: xps.append(int(num))

    def dfs(op,operator,xps):
        # op 연산
        while op in xps:
            # 피연산자 찾기
            i = xps.index(op)
            if op=='+': r = xps[i-1]+xps[i+1]
            elif op=='-': r = xps[i-1]-xps[i+1]
            elif op=='*': r = xps[i-1]*xps[i+1]
            xps = xps[:i-1]+[r]+xps[i+2:]
        # operator 사본에서 op 제외
        next_op = operator[:]
        next_op.remove(op)
        if not next_op: return abs(xps[0])# abs 값 리턴
        # 재귀
        v = []
        for i in next_op:
            v.append(dfs(i,next_op,xps[:]))
        return max(v)

    v = []
    for i in operator:
        v.append(dfs(i,operator[:],xps[:]))
    return max(v)

print(solution("50*6-3*2"))
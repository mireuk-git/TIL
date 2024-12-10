# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack=[]
    length=len(number)-k
    for i,n in enumerate(list(map(int,number))):
        while stack and int(stack[-1])<n and len(stack)+len(number[i:])>length:
            stack.pop()
        stack.append(n)
        if len(stack)>length: stack.pop()
    for i in range(len(stack)):stack[i]=str(stack[i])
    return ''.join(stack)

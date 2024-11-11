#https://school.programmers.co.kr/learn/courses/30/lessons/12945


'''             #runtime error
fib_list=[0,1]
def fibonacci(n):
    if n<len(fib_list): 
        return fib_list[n]
    else: 
        fib_list.append(fibonacci(n-1)+fibonacci(n-2))
        return fib_list[n]
def solution(n):         
        return fibonacci(n)%1234567
'''

def solution(n):
    prev, Next, tmp = 0,1,0
    for i in range(n-1):
        tmp = Next+prev
        prev = Next
        Next = tmp
    return Next%1234567
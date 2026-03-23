# https://www.acmicpc.net/problem/33557

import sys
input = sys.stdin.readline

t=int(input().strip())
for test_case in range(t):
    a,b = input().strip().split()
    a_digit,b_digit = [],[]
    for i in range(len(a)-len(b)): b_digit.append(1)
    for i in range(len(b)-len(a)): a_digit.append(1)
    a_digit+=map(int,list(a))
    b_digit+=map(int,list(b))
    cal1 = ''
    for i in range(len(a_digit)):
        cal1+=str(a_digit[i]*b_digit[i])
    if int(cal1)==int(a)*int(b): print(1)
    else: print(0)

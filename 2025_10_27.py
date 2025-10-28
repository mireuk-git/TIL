# https://www.acmicpc.net/problem/4466
# 4466

import sys
input=sys.stdin.readline

def evaluate(expr):
    stack=[]
    i=0
    while i < len(expr):
        if expr[i] == '(': stack.append(i+1)
        if expr[i] == ')':
            expr=expr[:stack[-1]-1]+evaluate_sub(expr[stack[-1]:i])+expr[i+1:]
            i=stack[-1]-1
            del stack[-1]
        i+=1
    if len(expr)==1: return expr
    return evaluate_sub(expr)

def evaluate_sub(expr):
    while '!' in expr:
        i=expr.find("!")
        if expr[i+1]=='t': expr=expr[:i]+'f'+expr[i+2:]
        else: expr=expr[:i]+'t'+expr[i+2:]
        
    if len(expr)==1: return expr

    if expr[1]=='|':
        if expr[0]=='t' or expr[2]=='t': return 't'
        else: return 'f'
    elif expr[1]=='&':
        if expr[0]=='t' and expr[2]=='t': return 't'
        else: return 'f'


x=int(input().strip())
for test_case in range(1,x+1):
    expr,expected=input().strip().split(" = ")
    eval_result = evaluate(expr)
    if eval_result == expected: result = "Good"
    else: result = "Bad"
    print(f"{test_case}: {result} brain")

    
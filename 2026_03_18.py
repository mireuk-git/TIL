# https://www.acmicpc.net/problem/3733
'''
while True:
    try:
        n,s = map(int,input().split())
        print(int(s/(n+1)))
    except EOFError:
        break
'''
# https://www.acmicpc.net/problem/21614

import sys
input = sys.stdin.readline

while True:
    instruction = input().strip()
    if instruction=='99999': break
    d_code=int(instruction[0])+int(instruction[1])
    steps=int(instruction[2:])
    if d_code%2==1:
        direction='left'
    elif d_code>0:
        direction='right'
    print(direction, steps)
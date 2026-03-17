# https://www.acmicpc.net/problem/4134

def isPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0: return False
    return True

import sys
input = sys.stdin.readline

t=int(input())
for i in range(t):
    n = int(input())
    if n<=2: print(2)
    else: 
        j = n
        while not isPrime(j): j+=1
        print(j)
# https://www.acmicpc.net/problem/9771
# 9771
'''
import sys

word=sys.stdin.readline().strip()
count=0
text=sys.stdin.readlines()
for line in text:
    count+=line.count(word)
print(count)
'''
# https://www.acmicpc.net/problem/10829
# 10829
'''
n=int(input())
print(bin(n)[2:])
'''
'''
n=int(input())
tmp=n
b=''
while tmp>0:
    b+=str(tmp%2)
    tmp//=2
b=b[::-1]
print(b)
'''
# https://www.acmicpc.net/problem/12711
# 12711

n=int(input())
for test_case in range(1,n+1):
    p,k,l=map(int,input().split())
    freq=list(map(int,input().split()))
    freq.sort(reverse=True)
    c=0
    for i in range(l):
        c+=freq[i]*(i//k+1)
    print(f"Case #{test_case}:",c)
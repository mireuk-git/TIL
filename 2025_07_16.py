# https://www.acmicpc.net/problem/15814
# 15814
'''
s=input()
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    a,b=min(a,b),max(a,b)
    if a==b: continue
    s=s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]
    print(s)
'''
# https://www.acmicpc.net/problem/11976
# 11976
'''
l=[list(map(int,input().split())) for _ in range(4)]
r=[0]
for i in l[::-1]:
    r.append(i[1]-i[0]+r[-1])
r=r[-2:0:-1]
for i in r: print(i)
'''

# https://www.acmicpc.net/problem/11288
# 11288

n,a,b=map(int,input().split())
encrypted=input()
offset=a**b%26
decrypted=''
for i in encrypted:
    if i!=' ':
        i=ord(i)-offset
        if i<65: i+=26
        i=chr(i)
    decrypted+=i
print(decrypted)

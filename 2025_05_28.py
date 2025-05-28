# https://www.acmicpc.net/problem/20154
# 20154
'''
stroke={
    'A':3,"B":2,"C":1,"D":2,"E":3,"F":3,"G":3,
    "H":3,"I":1,"J":1,"K":3,"L":1,"M":3,"N":3,
    "O":1,"P":2,"Q":2,"R":2,"S":1,"T":2,"U":1,
    "V":1,"W":2,"X":2,"Y":2,"Z":1
}
s=input()
l=[stroke[i] for i in s]
while len(l)>1:
    l2=[]
    for i in range(0,len(l)//2*2,2):
        l2.append((l[i]+l[i+1])%10)
    if len(l)%2: l2.append(l[-1])
    l=l2
    del(l2)
if l[0]%2:
    print("I'm a winner!")
else: print("You're the winner?")
'''
# https://www.acmicpc.net/problem/11923
# 11923

n,c=map(int,input().split())
l=list(map(int,input().split()))

m=0
for i in range(n):
    s=0
    c=0
    for j in range(i,n):
        if s<=n-l[j]:
            s+=l[j]
            c+=1
    if c>m: m=c
print(m)
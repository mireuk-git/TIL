# https://www.acmicpc.net/problem/30034
# 30034

n=int(input())
char_Split=input().split()
m=int(input())
int_Split=input().split()
k=int(input())
merge=input().split()
s=int(input())
string=input()

tmp=''
l=[]
for i in string:
    if i==' ' or (i in char_Split+int_Split and i not in merge):
        if tmp:
            l.append(tmp)
            tmp=''
    else: tmp+=i
if tmp: l.append(tmp)

for i in l:
    print(i)
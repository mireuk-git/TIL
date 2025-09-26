# https://www.acmicpc.net/problem/1251
# 1251

s=input()
l=len(s)-1
can=set()
for idx1 in range(l-1):
    for idx2 in range(idx1+1,l):
        can.add(s[idx1:0:-1]+s[0]+s[idx2:idx1:-1]+s[l:idx2:-1])
can=list(can)
print(min(can))
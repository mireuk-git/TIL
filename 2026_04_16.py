# https://www.acmicpc.net/problem/20355

w = input()
count=0
for i in range(26):
    result=True
    for j in w:
        if (ord(j)+i)%26==1:
            result=False
            break
    if result:
        count+=1
if count==0: print("impossible")
else: print(count)
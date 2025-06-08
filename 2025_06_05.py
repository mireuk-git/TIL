# https://www.acmicpc.net/problem/14723
# 14723
'''
n=int(input())
a,b,s=1,1,1
while s<n:
    b+=1
    s+=b
for i in range(s,n,-1):
    a+=1
    b-=1
print(a,b)
'''
# https://www.acmicpc.net/problem/17288
# 17288

s=input()
c=0
for i in range(len(s)-2):
    flag=True
    for j in range(i,i+2):
            if int(s[j])!=int(s[j+1])-1: 
                flag=False
                break
    if flag:
        if i!=0 and int(s[i-1])==int(s[i])-1: flag=False
        elif i!=len(s)-3 and int(s[i+3])==int(s[i+2])+1: flag=False
    if flag: c+=1
print(c)
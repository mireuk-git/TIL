# https://www.acmicpc.net/problem/15721
# 15721

a=int(input())
t=int(input())
chant=input()

total,count,n=-1,0,2
while count<t:
    sentence='0101'+'0'*n+'1'*n
    for i in sentence:
        total+=1
        if i == chant: 
            count+=1
            if count>=t: break
    n+=1
print(total%a)


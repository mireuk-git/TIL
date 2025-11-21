# https://www.acmicpc.net/problem/31909
# 31909

n=int(input())
a=list(map(int,input().split()))
l={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7}
k=int(input())

for i in a:
    a_bin = bin(i)
    if a_bin.count("1")!=2: continue
    a_bin = "0"*(10-len(a_bin)) + a_bin[2:]
    left,right=10,10
    for j in range(8):
        if a_bin[j]=="1":
            if left==10: left=7-j
            else: 
                right=7-j
                break
    l[left],l[right]=l[right],l[left]

print(l[k])

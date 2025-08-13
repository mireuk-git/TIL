# https://www.acmicpc.net/problem/5679
# 5679
'''
h=int(input())
while h!=0:
    mh=h
    while h>1:
        if h%2:
            h=h*3+1
            if h>mh: mh=h
        else: h//=2
    print(mh)
    h=int(input())
'''
# https://www.acmicpc.net/problem/2596
# 2596

code=['000000','001111','010011','011100','100110','101001','110101','111010']
char=['A','B','C','D','E','F','G','H']
n=int(input())
message=input()
decoded=''
decode_fail=True
for i in range(n):
    decode_fail=True
    for j in range(len(code)):
        if sum(ch1==ch2 for ch1,ch2 in zip(code[j],message[6*i:6*(i+1)]))>=5:
            decoded+=char[j]
            decode_fail=False
            break
    if decode_fail: break

if decode_fail: print(i+1)
else: print(decoded)
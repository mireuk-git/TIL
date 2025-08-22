# https://www.acmicpc.net/problem/4900
# 4900

decode={
    "063":"0", "010":"1", "093":"2", "079":"3", 
    "106":"4", "103":"5", "119":"6", "011":"7",
    "127":"8", "107":"9"
    }
encode={
    "0":"063","1":"010","2":"093","3":"079",
    "4":"106","5":"103","6":"119","7":"011",
    "8":"127","9":"107"
    }
feed=input()
while feed!="BYE":
    a,b=feed.split("+")
    A=''
    for i in range(len(a)//3):
        A+=decode[a[i*3:(i+1)*3]]
    B=''
    for i in range(len(b)//3):
        B+=decode[b[i*3:(i+1)*3]]
    A=int(A)
    B=int(B)
    R=str(A+B)
    r=''
    for i in R:
        r+=encode[i]
    print(f"{feed}{r}")
    feed=input()
# https://www.acmicpc.net/problem/6052

s=int(input())
d1=s
while True:
    d1_divisor=[1]
    for i in range(2,int(d1**0.5)+1):
        if (d1%i==0): 
            d1_divisor.append(i)
            if i!=d1**0.5:
                d1_divisor.append(d1//i)
    d2=sum(d1_divisor)
    d2_divisor=[1]
    for i in range(2,int(d2**0.5)+1):
        if (d2%i==0):
            d2_divisor.append(i)
            if i!=d1**0.5:
                d2_divisor.append(d2//i)
    if sum(d2_divisor) == d1 and d1!=d2: break
    else: d1+=1
print(d1,d2)
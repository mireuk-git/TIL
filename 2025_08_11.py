# https://www.acmicpc.net/problem/30030
# 30030
'''
b=int(input())
a=b//11*10
print(a)
'''

# https://www.acmicpc.net/problem/6565
# 6565

feed=input()
while feed != "0+0=0":
    feed,c=feed.split("=")
    a,b=feed.split("+")
    a,b,c=map(int,(a[::-1],b[::-1],c[::-1]))

    if a+b==c: print("True")
    else: print("False")
    feed=input()
print("True")
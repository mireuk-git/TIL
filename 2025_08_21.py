# https://www.acmicpc.net/problem/10882
# 10882
'''
n=int(input())
time,d=input().split()
h,m=map(int,time.split(":"))
m+=h*60
D=float(d[3:])
for i in range(n):
    d=float(input()[3:])
    M=m+int(d*60)-int(D*60)
    H=M//60
    H%=24
    M%=60
    print(f"{H:02d}:{M:02d}")
'''
# https://www.acmicpc.net/problem/20116
# 20116

n,l=map(int,input().split())
x=list(map(int,input().split()))
x=x[::-1]
stable=True
w=x[0]
for i in range(1,len(x)):
    if w>=x[i]+l or w<=x[i]-l:
        stable=False
        break
    else: 
        w=(w*i+x[i])/(i+1)
if stable: print("stable")
else: print("unstable")
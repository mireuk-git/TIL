# https://www.acmicpc.net/problem/6147
# 6147
'''
import sys
input=sys.stdin.readline

n,b = map(int,input().strip().split())
h=[]
for i in range(n): h.append(int(input().strip()))
h.sort(reverse=True)

s=0
for cnt in range(n):
    s+=h[cnt]
    if s >= b:
        break
cnt+=1
print(cnt)
'''
# https://www.acmicpc.net/problem/19636
# 19636

w,l0,t=map(int,input().split())
d,l,a=map(int,input().split())

dw1 = w+d*(l-(l0+a))
if dw1>0:
    print(dw1, l0)
else: print("Danger Diet")

dl=l0
alive=True
for i in range(d):
    w+=l-(dl+a)
    if abs(l-dl-a)>t: dl += (l-(dl+a))//2
    if w<=0 or dl<=0:
        print("Danger Diet")
        alive=False
        break

if alive:
    if dl<l0:
        print(w,dl,"YOYO")
    else:
        print(w,dl,"NO")
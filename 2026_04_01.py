# https://www.acmicpc.net/problem/26307
'''
h,m = map(int,input().split())
print((h-9)*60+m)
'''
# https://www.acmicpc.net/problem/26502

crack = {'y':'a','a':'e','e':'i','i':'o','o':'u','u':'y',
         'Y':'A','A':'E','E':'I','I':'O','O':'U','U':'Y'}
n=int(input())
for i in range(n):
    s = input()
    replaced=""
    for j in s:
        if j in crack.keys(): replaced+=crack[j]
        else: replaced+=j
    print(replaced)

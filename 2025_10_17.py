# https://www.acmicpc.net/problem/12871
# 12871

s=input()
t=input()
if len(s)>len(t): s,t = t,s
len_s,len_t = len(s),len(t)
while len_s>0:
    len_t,len_s=len_s,len_t%len_s
gcd=len_t
len_s,len_t = len(s),len(t)
t*=len_s//gcd
s*=len_t//gcd
if s==t:print(1)
else: print(0)
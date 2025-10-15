# https://www.acmicpc.net/problem/32855
# 32855

a=input()
b=input()

a_int,a_deci = map(int,a.split('.'))
b_int,b_deci = map(int,b.split('.'))

if a_int>b_int: 
    int_tuple = '>'
elif a_int==b_int:
    if a_deci>b_deci: int_tuple = '>'
    elif a_deci<b_deci: int_tuple = '<'
    else: int_tuple='='
else: int_tuple='<'

a,b=float(a),float(b)
if a>b: 
    deci='>'
    return_value=a
elif a<b: 
    deci='<'
    return_value=b
else: 
    deci='='
    return_value=a

if int_tuple==deci:print(return_value)
else: print(-1)
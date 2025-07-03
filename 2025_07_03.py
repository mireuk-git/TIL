# https://www.acmicpc.net/problem/3028
# 3028
'''
shuffle=input()
l=[True,False,False]
for i in shuffle:
    if i=='A':
        l[0],l[1]=l[1],l[0]
    elif i=='B':
        l[1],l[2]=l[2],l[1]
    else:
        l[0],l[2]=l[2],l[0]
for i in range(3):
    if l[i]: print(i+1)
'''
# https://www.acmicpc.net/problem/12400
# 12400

translator={'a':'y','b':'h','c':'e','d':'s','e':'o',
            'f':'c','g':'v','h':'x','i':'d','j':'u',
            'k':'i','l':'g','m':'l','n':'b','o':'k',
            'p':'r','q':'z','r':'t','s':'n','t':'w',
            'u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
t=int(input())
for case_num in range(1,t+1):
    s=input()
    print(f"Case #{case_num}: ",end='')
    for i in s:
        if i==' ': print(' ',end='')
        else: print(translator[i],end='')
    print()
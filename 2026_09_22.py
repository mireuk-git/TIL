# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n,t,m,p):
    def convert(x,n):
        ch = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        r=''
        while x>=n:
            c = x%n
            if c>=10: c=ch[c]
            r += str(c)
            x//=n
        if x>=10: r+=ch[x]
        else: r+=str(x)
        return r[::-1]
    
    i = p-1
    num = 0
    string = ''
    result = ''
    for _ in range(t):
        while len(string)<=i: 
            string += convert(num,n)
            num+=1
        result+=string[i]
        i+=m
    return result

print(solution(2,4,2,1))
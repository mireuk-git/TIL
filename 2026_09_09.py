# https://school.programmers.co.kr/learn/courses/30/lessons/62048
'''
def solution(w,h):
    answer=w*h
    def gcd(a,b):
        while b>0:
            if b>a: a,b = b,a
            tmp = b
            b = a%b
            a = tmp
        return a
    n=gcd(w,h)
    answer-=w+h-n
    return answer

print(solution(8,12))
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    min_l=len(s)
    for n in range(1,len(s)//2+1):
        i=0
        new_string = ""
        while (i<len(s)):
            if (s[i:i+n]==s[i+n:i+2*n]):
                cnt = 1
                while (s[i:i+n]==s[i+n:i+2*n]):
                    i+=n
                    cnt+=1
                new_string+=str(cnt)
            new_string+=s[i:i+n]
            i+=n
        if min_l>len(new_string): min_l = len(new_string)
    return min_l

s="abcabcabcabcdededededede"
print(solution(s))
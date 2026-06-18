# https://school.programmers.co.kr/learn/courses/30/lessons/181187

def solution(r1,r2):
    def count_circle(r, edge):
        x,y = 0,r
        count = 0
        while y>0:
            while x**2+y**2>r**2: y-=1
            if edge==False and x**2+y**2==r**2: y-=1
            count+=max(0,y)
            x+=1
        return count*4
    
    d1 = count_circle(r1, False)
    d2 = count_circle(r2, True)
    return d2-d1

print(solution(1,2))
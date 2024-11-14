#https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    answer, a=arr[0],arr[0]
    for b in arr:
        answer*=b
        if a<b: a,b=b,a
        while b!=0:
            a,b=b,a%b
        answer//=a
        a=answer
    return answer
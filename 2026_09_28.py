# https://school.programmers.co.kr/learn/courses/30/lessons/132265
'''
def solution(topping):
    left,right = 0,len(topping)
    while (left<right):
        mid = (left+right)//2
        leftset = set(topping[:mid])
        rightset = set(topping[mid:])
        if len(leftset)<len(rightset):
            left = mid+1
        else: right = mid

    i = left
    leftset,rightset = set(topping[:i]),set(topping[i:])
    count = 0
    while len(leftset)==len(rightset):
        count+=1
        i+=1
        leftset = set(topping[:i])
        rightset = set(topping[i:])
    return count
'''

def solution(topping):
    low,high = 0,len(topping)
    while (low<high):
        mid = (low+high)//2
        leftset = set(topping[:mid])
        rightset = set(topping[mid:])
        if len(leftset)<len(rightset):
            low = mid+1
        else: high = mid
    left = low

    low,high = 0,len(topping)
    while (low<high):
        mid = (low+high)/2
        if mid>int(mid): mid=int(mid)+1
        else: mid = int(mid)
        leftset = set(topping[:mid])
        rightset = set(topping[mid:])
        if len(leftset)>len(rightset):
            high = mid-1
        else: low = mid
    right = high
    
    return right-left+1

topping = [1, 2, 1, 3, 1, 4, 1, 2]	
print(solution(topping))
        
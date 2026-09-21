# https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''
def solution(people, limit):
    people.sort()
    target = limit//2
    left,right = 0,len(people)
    while left<right:
        mid = (left+right)//2
        if people[mid]<=target:
            left = mid+1
        else:
            right = mid
    boat = left//2
    boat += len(people)-left
    return boat

people = [70, 80, 50]
print(solution(people,100))
'''

def solution(people, limit):
    people.sort()
    left,right = 0,len(people)-1
    boat = 0
    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
        right-=1
        boat+=1
    return boat

people = [70, 50, 80, 50, 50, 50, 50, 60, 40, 50]
print(solution(people,100))
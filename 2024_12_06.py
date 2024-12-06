#https://school.programmers.co.kr/learn/courses/30/lessons/42746#qna
from functools import cmp_to_key
def solution(numbers):
    num_str = [str(i) for i in numbers]
    num_str.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))
    return str(int(''.join(num_str)))
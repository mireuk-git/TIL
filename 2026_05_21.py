# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    column_index={"code":0,"date":1,"maximum":2,"remain":3}
    data.sort(key=lambda x: x[column_index[ext]])
    for i in range(len(data)):
        if data[i][column_index[ext]]>val_ext:
            break
    view=data[:i]
    view.sort(key=lambda x:x[column_index[sort_by]])
    return view
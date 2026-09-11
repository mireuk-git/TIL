# https://school.programmers.co.kr/learn/courses/30/lessons/42888https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    user = {} #{uid:name}
    for i in range(len(record)):
        record[i] = record[i].split()
        if record[i][0] in ["Enter", "Change"]:
            user[record[i][1]] = record[i][2]

    result = []
    for i in range(len(record)):
        if record[i][0] == "Enter":
            result.append(user[record[i][1]]+"님이 들어왔습니다.")
        elif record[i][0] == "Leave":
            result.append(user[record[i][1]]+"님이 나갔습니다.")
    return result

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

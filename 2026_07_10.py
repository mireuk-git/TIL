# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    book_time.sort(key=lambda x: x[0])
    rooms=["00:00"]
    for t in book_time:
        h,m = map(int,t[1].split(":"))
        m+=10
        if m>=60: 
            m-=60
            h+=1
            
        new=True
        for i in range(len(rooms)):
            if rooms[i]<=t[0]:
                rooms[i] = f"{h:02d}:{m:02d}"
                new=False
                break
        if new: rooms.append(f"{h:02d}:{m:02d}")
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil

def time_convert(time):
    h,m = map(int,time.split(":"))
    return h*60+m

def solution(fees,records):
    info = {} # num:[in,out_bool,time]
    for record in records:
        time,num,detail = record.split()
        if num not in info.keys(): info[num]=[0,False,0]
        if detail == "IN":
            info[num][0] = time_convert(time)
            info[num][1] = False
        elif detail == "OUT" and num in info.keys():
            info[num][1] = True
            info[num][2] += time_convert(time)-info[num][0]
    for i in info.keys():
        if info[i][1]==False:
            info[i][1] = True
            info[i][2] += time_convert("23:59")-info[i][0]

    l = []
    for i in info.keys():
        if info[i][2]>fees[0]:
            fee = fees[1]+ceil((info[i][2]-fees[0])/fees[2])*fees[3]
        else:
            fee = fees[1]
        l.append([i,fee])
    l.sort(key = lambda x: x[0])
    t=[l[i][1] for i in range(len(l))]
    return t


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees,records))


        
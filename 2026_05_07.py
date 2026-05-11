'''def solution(video_len, pos, op_start, op_end, commands):
    def skip_op(pos,start,end):
        if start[0]<=pos[0] and pos[0]<=end[0] and start[1]<=pos[1] and pos[1]<=end[1]:
            pos=[int(op_end[0:2]),int(op_end[3:4])]
        return pos
    
    vlen = list(map(int,video_len.split(":")))
    pos=list(map(int,pos.split(":")))
    start=list(map(int,op_start.split(":")))
    end=list(map(int,op_end.split(":")))
    
    for c in commands:
        pos=skip_op(pos,start,end)
        if c == "skip":
            pos[1]+=10
            if pos[1]>60: 
                pos[0]+=1
                pos[1]-=60
            if pos[0]>vlen[0] or (pos[0]==vlen[0] and pos[1]>vlen[1]):
                pos=vlen
        elif c == "prev":
            pos[1]-=10
            if pos[1]<0:
                if pos[0]==0: pos=[0,0]
                else:
                    pos[0]-=1
                    pos[1]+=60
    answer = "{}:{}".format(pos[0],pos[1])
    return answer


video_len="34:33"
pos="13:00"
op_start="00:55"
op_end="02:55"
commands=["next", "prev"]
print(solution(video_len,pos,op_start,op_end,commands))'''


'''
def solution(strings, n):
    second=[]
    for i in strings: second.append(strings[n])
    z = sorted(zip(strings,second),key=lambda x: (x[1], x[0]))
    strings,second = zip(*z)
    print(second)
    return strings

strings=["sun", "bed", "car"]	
n=1
print(solution(strings,n))
'''
'''
def solution(arr):
    answer = arr
    if len(answer)>0:
        answer.remove(min(answer))
    else: answer=[-1]
    return answer

arr=[4,3,2,1]
print(solution(arr))
'''
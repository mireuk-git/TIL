#https://school.programmers.co.kr/learn/courses/30/lessons/150370

'''
def solution(today, terms, privacies):
    answer = []
    t={}
    for i in range(len(terms)): 
        tmp=terms[i].split()
        t[tmp[0]]=tmp[1]						#key: term_type, value: 유효기간
    del tmp
    for i in range(len(privacies)): 
        p=privacies[i].split()  				#p[0]: 수집날짜, p[1]: term_type
        p[0]=list(map(int,p[0].split("."))) 	#날짜 쪼개기
        p[0][1]+=int(t[p[1]])   				#만료날짜 구하기
        if p[0][1]>12:
            p[0][0]+=p[0][1]//12
            p[0][1]%=12
            if p[0][1]==0:
                p[0][0]-=1
                p[0][1]=12
        termdate=f"{p[0][0]}.{p[0][1]:02d}.{p[0][2]:02d}"
        if today>=termdate: 					#만료여부 확인
            answer.append(i+1)            
    return answer
'''

def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
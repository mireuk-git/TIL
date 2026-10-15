# https://school.programmers.co.kr/learn/courses/30/lessons/17686

def separate(file):
    # 각 file에 대해 head/number/tail 나누기
    # head는 문자로만 이루어짐, 처음 나오는 숫자는 number
    i=0
    while i<len(file):
        if file[i].isdigit():break
        i+=1
    head = file[:i]
    j=i+1
    while j<len(file):
        if not file[j].isdigit():break
        j+=1
    number = int(file[i:j])
    tail = file[j:]
    return [head,number,tail]

def solution(files):
    tmp=files[:]
    for i in range(len(tmp)):
        # head와 tail에서 대소문자를 구분하지 않음
        tmp[i] = tmp[i].lower()
        tmp[i] = separate(tmp[i])+[i]
    # head, number, tail 순으로 정렬
    files = [f for _,f in sorted(zip(tmp,files), key = lambda x: [x[0][0],x[0][1],x[0][3]])]
    return files
    
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
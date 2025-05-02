# https://www.acmicpc.net/problem/1788
# 1788
'''
n=int(input())
f0,f1=0,1
if n==0: 
    print(0)
    print(0)
elif n<0:
    for i in range(-1,n-1,-1):
        f0,f1=f1-f0,f0
    if f0>0: print(1)
    else: print(-1)
    print(abs(f0)%1000000000)
else:
    for i in range(2,n+1):
        f0,f1=f1,f0+f1
    print(1)
    print(f1%1000000000)
'''
'''
MOD = 1000000000

def matrix_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def matrix_pow(matrix, n):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while n > 0:
        if n % 2 == 1:
            result = matrix_mul(result, matrix)
        matrix = matrix_mul(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n > 0:
        mat = [[1, 1], [1, 0]]
        return matrix_pow(mat, n)[0][1]
    else:
        # 음수 피보나치: F(-n) = (-1)^(n+1) * F(n)
        pos_fib = fibonacci(-n)
        return (-1)**(n + 1) * pos_fib

n = int(input())
fib = int(fibonacci(n))

if fib == 0:
    print(0)
else:
    print(1 if fib > 0 else -1)
print(abs(fib) % MOD)
'''
# https://www.acmicpc.net/problem/9518
# 9518

r,s=map(int,input().split())
mat=[]
for i in range(r): mat.append(list(input()))
clap=0
max=0
for i in range(r):
    for j in range(s):
        c=0
        if i<r-1:
            if mat[i+1][j]=='o':c+=1
            if j<s-1 and mat[i+1][j+1]=='o':c+=1
            if j>0 and mat[i+1][j-1]=='o':c+=1
        if j<s-1 and mat[i][j+1]=='o': c+=1
        if mat[i][j]=='o': clap+=c

        else:
            if i>0:
                if mat[i-1][j]=='o': c+=1
                if j>0 and mat[i-1][j-1]=='o': c+=1
                if j<s-1 and mat[i-1][j+1]=='o': c+=1
            if j>0 and mat[i][j-1]=='o': c+=1
            if max<c: max=c
print(clap+max)

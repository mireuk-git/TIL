# https://www.acmicpc.net/problem/32684
'''
p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

p1_score = 13*p1[0]+7*p1[1]+5*p1[2]+3*p1[3]+3*p1[4]+2*p1[5]
p2_score = 13*p2[0]+7*p2[1]+5*p2[2]+3*p2[3]+3*p2[4]+2*p2[5] + 1.5
if p1_score > p2_score: print("cocjr0208")
else: print("ekwoo")
'''

# https://www.acmicpc.net/problem/25305
'''
n,k = map(int,input().split())
x = list(map(int,input().split()))
x.sort(reverse=True)
print(x[k-1])
'''

def heapify(arr, index, heapsize):
    largest = index
    left = 2*index+1
    right = 2*index+2
    if left < heapsize and arr[left] > arr[largest]: largest = left
    if right < heapsize and arr[right] > arr[largest]: largest = right
    if largest != index:
        arr[largest],arr[index] = arr[index],arr[largest]
        heapify(arr,largest,heapsize)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)
    return arr

n,k = map(int,input().split())
x = list(map(int,input().split()))
heapsort(x)
print(x)
print(x[-k])

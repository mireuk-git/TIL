# https://www.acmicpc.net/problem/10866
# 10866
'''
from collections import deque
import sys
input=sys.stdin.readline

n=int(input().strip())
d=deque()
for i in range(n):
    command=input().strip()
    if 'push' in command:
        command,x=command.split()
        if command=='push_front': d.appendleft(int(x))
        elif command=='push_back': d.append(int(x))
    elif command=='pop_front': 
        if len(d): print(d.popleft())
        else: print(-1)
    elif command=='pop_back': 
        if len(d): print(d.pop())
        else: print(-1)
    elif command=='size': print(len(d))
    elif command=='empty': 
        if len(d): print(0)
        else: print(1)
    elif command=='front': 
        if len(d): print(d[0])
        else:print(-1)
    elif command=='back': 
        if len(d): print(d[-1])
        else: print(-1)
'''

import sys
input=sys.stdin.readline

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self,value):
        node=Node(value)
        if self.tail is None:
            self.head=self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self._size+=1

    def appendleft(self,value):
        node=Node(value)
        if self.head is None:
            self.head=self.tail=node
        else:
            self.head.prev=node
            node.next=self.head
            self.head=node
        self._size+=1

    def pop(self):
        if self.tail is None:
            return -1
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else: 
            self.tail.next = None
        self._size-=1
        return value
    
    def popleft(self):
        if self.head is None:
            return -1
        value=self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else: 
            self.head.prev = None
        self._size-=1
        return value
    
    def __len__(self):
        return self._size
    
    def front(self):
        if self.head is not None:
            return self.head.value
        else: return -1
    
    def back(self):
        if self.tail is not None:
            return self.tail.value
        else: return -1

n=int(input().strip())
d=Deque()
for i in range(n):
    command=input().strip()
    if 'push' in command:
        command,x=command.split()
        if command=='push_front': d.appendleft(int(x))
        elif command=='push_back': d.append(int(x))
    elif command=='pop_front': print(d.popleft())
    elif command=='pop_back': print(d.pop())
    elif command=='size': print(len(d))
    elif command=='empty': 
        if len(d): print(0)
        else: print(1)
    elif command=='front': print(d.front())
    elif command=='back': print(d.back())
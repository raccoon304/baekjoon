from collections import deque 
import sys 
input = sys.stdin.readline

N = int(input())
queue = deque(map(int, input().rstrip().split()))
stack = deque()
i = 1 
while queue:
    if queue and queue[0] == i:
        queue.popleft()
        i += 1 
    else:
        stack.append(queue.popleft())
    while stack and stack[-1] == i:
        stack.pop()
        i+=1
        
print('Nice' if not stack else 'Sad')
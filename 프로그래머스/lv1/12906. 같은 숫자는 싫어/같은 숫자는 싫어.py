from collections import deque 

def solution(arr):
    answer = []
    q = deque(arr)
    answer.append(q.popleft())  # 큐 정의 후, 1번째 요소 기준점으로 잡기
    
    for i in range(1,len(arr)):  # 1번째껀 넣었으니 빼고 loop
        next = q.popleft() 
        if next == answer[-1]:
            continue 
        else:
            answer.append(next) 
        
    
    return answer
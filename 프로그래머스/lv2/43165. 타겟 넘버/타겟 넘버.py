from collections import deque 

def solution(numbers, target):
    answer = 0
    q = deque()
    n = len(numbers)
    
    q.append([numbers[0], 0])    #덧셈연산
    q.append([-1*numbers[0],0])  #뺄셈연산
    
    while q:
        temp, idx = q.popleft()
        idx +=1 
        if idx <n :
            q.append([temp+numbers[idx],idx])    # < 구조로 뻗어나감 
            q.append([temp-1*numbers[idx],idx])  
        else:
            if temp == target:
                answer +=1
    return answer
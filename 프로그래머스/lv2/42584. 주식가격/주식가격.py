# 가격이 떨어지지 않은 기간 
from collections import deque 

def solution(prices):
    queue = deque(prices) 
    answer = []
    
    while queue:
        price=queue.popleft() 
        sec=0
        for q in queue:
            sec +=1
            if price > q:
                break 
                
        answer.append(sec)
    return answer 

# prices= [1, 2, 3, 2, 3]
# temp=[i for i in prices[3+1:] if i >=2]
# print(temp)
# print(len(temp))
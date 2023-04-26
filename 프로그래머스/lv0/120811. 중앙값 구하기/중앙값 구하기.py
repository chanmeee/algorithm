import math 

def solution(array):
    answer = 0
    
    N = len(array)
    
    # 1) 정렬 
    array = sorted(array)
    
    if N % 2 == 0: 
        answer = (array[(N/2)-1] + array[(N/2)] ) / 2
    elif N % 2 != 0: 
        answer = array[math.floor(N/2)] 
        
    return answer
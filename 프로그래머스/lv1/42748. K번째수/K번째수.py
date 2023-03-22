def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        
        sorted_l = sorted(array[i-1:j])
        answer.append(sorted_l[k-1])
    
    
    
    return answer
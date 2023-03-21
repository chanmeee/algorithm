def solution(sizes):
    answer = 0
    w_list=[]
    h_list=[]
    
    for i in range(len(sizes)):
        w_list.append(max(sizes[i])) 
        h_list.append(min(sizes[i]))
        
    answer = max(w_list) * max(h_list)
    
    return answer
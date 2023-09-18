def solution(arr, query):
    answer = arr 
    
    for i, q in enumerate(query):
        if i % 2 == 0:
            #idx = answer.index(q)
            #print(answer) 
            answer = answer[:(q+1)] 
            #print(q, idx, answer)
            
        elif i % 2 == 1:
            #idx = answer.index(q) 
            #print(answer)
            answer = answer[q:] 
            #print(q, idx, answer)
    return answer 
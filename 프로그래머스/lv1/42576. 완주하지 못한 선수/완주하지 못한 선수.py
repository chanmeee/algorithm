def solution(participant, completion):
    answer = ''
    dict1 = {}  # participant 
    #dict_c = {}  # completion 
    
    for p in participant:
        if p in dict1:
            dict1[p] += 1
        else:
            dict1[p] = 1
    for c in completion:
        if c in dict1:
            dict1[c] -= 1
        else:
            dict1[c] = 1
                        
    #print(dict1)
    for k,v in dict1.items():
        if v !=0:
            return k
    
    
    
    #return answer
def solution(common):
    answer = 0
    
    # 등차일 경우
    if common[1]-common[0] == common[-1]-common[-2] :
        d = common[1]-common[0] 
        answer = common[-1]+d 
    else :
        r = common[1]/common[0] 
        answer = common[-1]*r 
    
    return answer 
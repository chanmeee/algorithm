# 번호는 체격 순 
# 바로 앞번호나 바로 뒷번호에게만 빌려줄 수 있음 ex) 4: 3 or 5

# 1:05 start  1:17 Try1(failed #13, #14)
# 전체 학생의 수 n, 
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 최대한 많이 체육수업 듣도록 

def solution(n, lost, reserve):
    answer = 0
        
    # 안 잃어버린 경우 
    answer += (n - len(lost))

    # 잃어버렸는데 여벌 있는 경우
    lostrev = [i for i in lost if i in reserve]
    answer += len(lostrev)

    for i in lostrev:
        reserve.remove(i)
        lost.remove(i)
            
    # 잃어버렸는데 여벌도 빌릴 수 없는 경우 
    ## 정렬!!
    lost = sorted(lost)
    reserve = sorted(reserve)
        
        
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer +=1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer +=1
    
    
    return answer


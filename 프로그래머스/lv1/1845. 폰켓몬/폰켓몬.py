# nums: N마리 폰켓몬의 종류 번호가 담긴 배열 
# 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다  

def solution(nums):
    
    answer = 0
    N = len(nums)
    
    # N/2 <= 포켓몬 가짓수 
    if N/2 <= len(set(nums)) :
        answer = N/2
        
    # N/2 > 포켓몬 가짓수
    elif N/2 > len(set(nums)) :
        answer = len(set(nums)) 

    answer = int(answer)
    return answer
    
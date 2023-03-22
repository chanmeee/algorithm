def solution(numbers):
    answer = ''
    
    # 1) 문자열로 변환 
    numbers = map(str, numbers)
    
    # 2) 사전 값으로 정렬  ex) 9부터 1까지
    numbers = sorted(numbers, key= lambda num :num*3,reverse=True)  # 단, 숫자*3 해줌 (30보다 3이 먼저 와야하므로)
    
    # 3) 붙이기 
    answer = str(int(''.join(numbers)))  # 0000 -> 0 나오도록 str을 int로 바꿨다가 다시 str로 변환 
    
    return answer
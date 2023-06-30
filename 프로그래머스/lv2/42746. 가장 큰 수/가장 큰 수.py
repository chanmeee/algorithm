def solution(numbers):
    answer = ''
    
    # 1) 문자열 변환
    numbers = map(str, numbers) 
    
    # 2) 알파벳순 정렬
    numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
    print(numbers)  
    
    # 3) 붙이기 
    answer = str(int(''.join(numbers)))
    
    return answer


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
def solution(num1, num2):
    answer = 0
    if num1 >=0 and num1 <=100:
        if num2 >=0 and num2 <=100:
            answer = num1*num2 
            return answer
        else:
            raise ValueError 
import math 

def solution(N, number):
    answer = 0
    set_list = [] 
    
    for cnt in range(1,9):
        partial_set = set()
        
        # 이어붙여 만드는 경우
        partial_set.add(int(str(N)*cnt))
        
        # 사칙연산 이용하는 경우 
        for i in range(cnt - 1):
            for op1 in set_list[i]: 
                for op2 in set_list[-i - 1]:
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0:
                        partial_set.add(op1 / op2)
        # 만든 숫자 붙이기
        set_list.append(partial_set)
        
        
        # 만들어진 숫자 중 number 있는지 확인 
        if number in partial_set:
            return cnt 
        
    return -1 
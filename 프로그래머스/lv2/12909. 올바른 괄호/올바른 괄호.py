def solution(s):
        
    stack = []
    
    for i in s : 
        # 여는 괄호이면, stack에 쌓기 
        if i == '(': 
            stack.append(i) 
        # 닫는 괄호이면, stack 맨 오른쪽 확인 후 제거 
        elif i == ')' and stack==[]:
            stack.append(i)  
        elif i == ')' and stack[-1] == '(':
            stack.pop(-1) 
    
    if stack != []: 
        return False  
    else: 
        return True 
    
    # 닫힌 괄호 나오면, stack의 가장 최근(오른쪽)만 확인 -> 쌍이 맞나? 
    # 맞으면 -> stack에서 해당 요소 제거
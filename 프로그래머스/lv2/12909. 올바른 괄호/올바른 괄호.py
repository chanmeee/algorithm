def solution(s):
    
    from collections  import deque 
    que = deque(s)   # leftpop() 쓰려면 deque여야 함 list에는 적용 불가능 
    stack = [] 
    answer = True 
    
    while que:  # que가 비어있지 않으면 
        temp = que.popleft() 
        
        # 열린 괄호이면 
        if temp == '(':
            stack.append(temp)
        
        # 닫힌 괄호이면 
        elif temp == ')' and stack and stack[-1] == '(':
            stack.pop() 
        else: 
            return False 
    
    # stack에 남아있는 괄호가 있으면 (다 처리안된 경우)
    if stack : 
        return False 
    else:
        return True 
    
    

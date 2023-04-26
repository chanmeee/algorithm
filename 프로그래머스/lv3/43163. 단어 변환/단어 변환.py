# 줄줄이 땅콩 -> dfs 써야겠다 (공항티켓 문제랑 비슷)
from collections import deque 

def solution(begin, target, words):
    answer = 0
    
    # words 리스트에 target 단어가 없는 경우, 0 반환
    if target not in words:
        return 0 
    
    q = deque() 
    q.append((begin,0)) 
    
    while q:
        visited = [0]*len(words)
        b_word,idx = q.popleft() 
        
        if b_word==target:
            break 
        
        # words 리스트의 "k번째 단어" 에 대해 
        for k in range(len(words)):
            # 단어 k의 "j번째 글자" 에 대해 
            for j in range(len(words[k])):
                if b_word[j] == words[k][j]:
                    visited[k] +=1
                    
        for k in range(len(visited)):         
            if visited[k] == (len(target)-1):
                q.append((words[k],idx+1)) 
                words[k] = str(idx)
    
    return idx 
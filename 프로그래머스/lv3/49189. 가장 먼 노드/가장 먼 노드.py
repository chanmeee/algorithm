# 최단경로문제 -> bfs - q 정의(현재 기준좌표), 1번 노드 시작 ~ deque 
# 인접노드 저장 - adj 정의 ~ defaultdict
# bfs 적용
# 이동수 계속 저장 후, max 값 저장, .count(max_value)를 리턴 
from collections import deque, defaultdict 

def solution(n, edge):
    answer = 0
    
    adj = defaultdict(list) 
    for i,j in edge:
        adj[i].append(j)
        adj[j].append(i) 
    
    q = deque() 
    q.append(1)  # 1부터 시작 
    moves=[0]*(n+1)  # 노드별 이동수
    moves[1] = 1 
    
    while q: 
        v = q.popleft() 
        
        for nv in adj[v]: 
            if moves[nv] != 0: # 처음 가는 경로 아니면 
                continue 
            if nv <=0 or nv>n:  # 1~n 범위 벗어나면
                continue 
            elif moves[nv] == 0 : 
                q.append(nv)
                moves[nv] = moves[v] + 1 
    
    max_m = max(moves)
    answer= moves.count(max_m)
        
    return  answer
# 송전탑의 개수 n, 전선 정보 wires 
# bfs 사용 

# 1) bfs 함수 정의
from collections import deque 

def bfs(graph, start, visited):
    q = deque([start])
    
    # 현재 노드 방문처리 
    visited[start] = True
    cnt = 0
    
    # 큐 빌 때까지 반복 
    while q:
        # 큐에서 원소 1개(s) 뽑기 
        s = q.popleft()
        cnt += 1 
        # 원소 s와 연결된 & 방문안한 원소들 큐에 삽입  
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True 
                
    return cnt 
    

def solution(n, wires):
    answer = n-2 # 송전탑의 개수 차이의 최댓값, 예를 들어, n=9일때 최대 절댓값은 두 전력망이 1과 8일때 즉 7
    
    for i in range(len(wires)):
        temp = wires.copy()
        # 연결상태, 방문여부 
        graph = [ [] for _ in range(n+1)]
        visited = [False] * (n+1) 
        
        # i번째 전선 제거 
        temp.pop(i)  
        
        # i번째 전선 제거 후 연결상태 
        for a,b in temp:
            graph[a].append(b)
            graph[b].append(a) 
            
        for idx, g in enumerate(graph):
            if g != []:
                start = idx
                break 
                
        # bfs를 이용, 시작점에서 다른 송전탑 탐색 
        cnts = bfs(graph,start,visited)
        other_cnts = n - cnts 
        answer = min(answer, abs(cnts - other_cnts)) 
         
        
    return answer
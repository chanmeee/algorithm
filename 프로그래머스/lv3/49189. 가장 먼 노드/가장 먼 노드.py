from collections import deque, defaultdict  

def solution(n, edge):
    answer = 0 
    
    adj = defaultdict(list)   # 인접 노드 저장
    visit = [0]*(n+1)  # 몇 번째 방문인지 저장 
    for a,b in edge:
        adj[a].append(b)
        adj[b].append(a) 
        
    visit[1]=1  # 노드1은 1번째 방문
    q = deque() 
    q.append(1)  # 첫 기준점은 1 
    
    while q:
        x = q.popleft()  # 큐의 제일 앞에 있는 거(노드) 빼내기 
        for next in adj[x]:  # 빼낸 노드와 연결된 다른 노드를 확인해가며, 
            if not visit[next] :   # 만일 해당 연결노드를 방문 안했으면,
                visit[next] = visit[x] + 1  # 기준점+1 로 방문index 저장
                q.append(next)  # 해당 연결노드는 큐에 append  ## 재귀! 
    
    max_v = max(visit) 
    cnt = visit.count(max_v) 
           
    return cnt 
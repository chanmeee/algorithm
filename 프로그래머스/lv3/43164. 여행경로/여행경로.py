# 경로문제 -> bfs XX => dfs 로 접근해야함 => 스택을 쓰자 
# q = ticket, 시작 "ICN"
# 경로 저장: defaultdict() 

from collections import deque, defaultdict 

def solution(tickets):
    path = []
    
    # 1) 이동가능한 경로 저장 후 
    graph = defaultdict(list)  
    for a,b in tickets:
        graph[a].append(b) 
        
    # 2) 도착점 리스트를 역순 정렬 
    for airport in graph.keys():
        graph[airport].sort(reverse=True)
    
    # 3) 출발은 인천 
    s = ["ICN"] # 출발은 인천  
    
    # 4) DFS 로 모든 노드 순회 
    while s :
        # 4-1) 스택에서 제일 위에꺼 꺼내 ex)[ICN, JFK] -> JFK
        top = s.pop()  
        
        # 4-2) top이 없거나, top에서 출발하는 티켓이 없으면, 
        ## path에 저장 & 더이상 탐색 안함  ex) JFK 끝? path에만 저장
        if top not in graph or not graph[top] :
            path.append(top) #[JFK]
            
        # 4-3) 그 다음 여정이 있으면, 
        ## top을 다시 스택에 넣고, top 도착점 중 가장 마지막 지점을 스택에 저장  ex) s = [ICN, JFK] 
        else:
            s.append(top) #[ICN,JFK]
            s.append(graph[top].pop()) #[ICN,JFK,MDR] 
            
    
    # 5) path를 뒤집어 반환 
    return path[::-1] 
# DFS/BFS # ex) 15 

## 모든 도로의 거리는 1 = 모든 간선의 비용이 1 => bfs 이용

import sys 
from collections import deque 
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

# 도로 정보 입력받기 
for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

# bfs로 탐색
def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0

    while q:
        # 도시를 popleft 
        now = q.popleft()
        
        # 현재 도시에서 이동할 수 있는 모든 도시를 확인 
        for next_node in graph[now]:
            # 아직 방문 안했다면, 방문처리 & 큐에 추가 & 최단거리 업데이트
            if not visited[next_node]:
                visited[next_node] = True 
                q.append(next_node)
                distance[next_node] = distance[now] +1
                # next 도시의 거리 값이 K이면, answer에 추가 
                if distance[next_node] == k:
                    answer.append(next_node)
        
        # 최단거리가 k인 도시가 하나도 없으면, -1 출력
        if len(answer) == 0:
            print(-1) 
        
        # 최단거리가 K인 도시가 있으면, 오름차순으로 출력
        else:
            answer.sort()
            for i in answer:
                print(i, end='\n')
                

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
            
bfs(x)
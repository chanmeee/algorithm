import sys 

# 최대 재귀 횟수(1000회) 제한을 풀어주기, 안하면 오류 발생
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
graph[0] = [0,0]
visited = [False for _ in range(n+1)]

count = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    
    graph[start].append(end)
    graph[end].append(start)
    # sort
    graph[start].sort()
    graph[end].sort()

def DFS(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        DFS(graph, i, visited)

print(count)

## 참고: https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%8011724%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-DFS
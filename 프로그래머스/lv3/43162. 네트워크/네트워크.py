#컴퓨터의 개수 n 
#연결에 대한 정보가 담긴 2차원 배열 computers
#네트워크의 개수를 return

def solution(n, computers):
    
    answer=0

    # 방문여부 체크하는 빈 boolean
    visited = [False] * n

    for comp in range(n):
        if visited[comp] == False: # 방문 안했으면
            DFS(n, computers, comp, visited)  #DFS로 최대한 깊이 연결된 컴퓨터들을 방문하고 빠져나오면, 그게 하나의 네트워크
            answer +=1

    return answer


def DFS(n, computers, comp, visited):
    visited[comp] = True  # 방문했다고 바꾸기
    
    for comp_connect in range(n):
        if comp != comp_connect and computers[comp][comp_connect] == 1:  # 연결된 컴퓨터
            if visited[comp_connect] == False:  #연결대상 방문 안했으면
                DFS(n, computers, comp_connect, visited)

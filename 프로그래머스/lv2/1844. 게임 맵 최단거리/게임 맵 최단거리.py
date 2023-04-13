from collections import deque 

def solution(maps):
    answer=0
    
    # 상하좌우 
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    # bfs 정의, 기준점 좌표 받기 
    def bfs(x,y):
        
        # 1) 큐를 정의한 다음, 시작노드를 넣는다
        ## 이때 큐는 collections의 deque를 이용
        queue = deque()  
        queue.append((x,y))  
        
        # 큐가 있을 때까지 (= 비기 전까지) 
        while queue: 
            
            # 2) 1번째를 빼낸다 VVVVVVVVVV 
            x, y = queue.popleft()
            
            # 3) 기준점 상하좌우 이동해 새 좌표 nx,ny
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i] 

                # 3-1) 새 좌표가 maps 범위 밖이면, continue
                if nx <0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) : continue 
                # 3-2) 새 좌표가 벽이면, continue 
                if maps[nx][ny] == 0: continue 
                # 3-3) 새 좌표가 새로운 길이면, 기존 좌표 제거 & queue에 추가 & 새 좌표값은 기존좌표+1
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1   
                    queue.append((nx,ny))  # 재귀 : 큐에 새 좌표를 넣는다. VVVV 
        
        return maps[len(maps)-1][len(maps[0])-1] 
    
    answer = bfs(0,0)
    return -1 if answer == 1 else answer 
    

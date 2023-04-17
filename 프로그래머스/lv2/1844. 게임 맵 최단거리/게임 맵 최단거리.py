# bfs 접근 : 큐 사용 
from collections import deque 

def solution(maps):
    answer = 0
    
    # 상하좌우 이동 
    dx=[0,0,1,-1]
    dy=[1,-1,0,0] 
    
    q = deque()
    q.append([0,0])  #시작점 (0,0) 
    
    while q: # q가 비기 전까지 
        x,y = q.popleft() # v: 현재 기준점 
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i] 
                        
            # 맵 범위 밖이면, 이동x
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) :
                continue 
            # 벽이 있으면, 이동x
            elif maps[nx][ny] == 0:  
                continue 
            # 처음 가는 길이고 이동가능하면, 이동 수를 적고 큐에 추가 
            elif maps[nx][ny] == 1:
                q.append([nx,ny])
                maps[nx][ny] = maps[x][y] +1 
    
    answer= maps[len(maps)-1][len(maps[0])-1]
    
    return -1 if answer==1 else answer


# TIL
# 인덱싱 유의: maps[x,y] 아니라 maps[x][y]로 해야 함! 
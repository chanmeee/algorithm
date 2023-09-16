def solution(n):
    answer = [ [0]*n for _ in range(n)]  # 빈 리스트 
    
    # 1) 방향 정의(나선형이므로 우하좌상) 
    dx = [0,1,0,-1]   # 아래 이동 시 x좌표 값 +1 됨! (리스트 인덱스)
    dy = [1,0,-1,0]
    
    # 2) 초기값 세팅 
    x,y = 0, 0
    answer[x][y] = 1
    k = 2  # 숫자 2부터 채워넣기 
    
    while k <= n*n:
        for i in range(4):
            while True:
                nx = x+dx[i]
                ny = y+dy[i]
                
                # (1) 범위 벗어났거나 (2) 이미 숫자 채운 경우, 이동 끝내기
                if nx>=n or nx<0 or ny>=n or ny<0 or answer[nx][ny]!=0:  
                    break   
                # (아니면) 숫자 채우고, x&y&k값 업데이트     
                else:
                    answer[nx][ny] = k 
                    x,y = nx,ny
                    k +=1
    return answer
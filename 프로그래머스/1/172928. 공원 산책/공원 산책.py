def solution(park, routes):
    answer = [] 
    x,y = 0,0
    
    # 시작점('S') 찾기 
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] =='S':
                x,y = i,j
                break 
    # 이동 방향 정의
    moves = {'N':(-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}
    
    # 이동 
    for r in routes:
        dx, dy = moves[r.split()[0]]  # moves 딕셔너리에서 해당 방향의 x,y 이동값 가져오기 
        steps = int(r.split()[1]) # 이동횟수
        
        # 위치 초기화 
        xx, yy = x,y
        canmove=True 
        
        # 이동 : 칸 범위 넘거나 장애물 만날 경우, 명령 무시 
        for _ in range(steps) :
            nx = xx + dx  # 이동한 x위치
            ny = yy + dy  # 이동한 y위치
            
            # 공원 범위 안 & 장애물 아닐 경우, 이동가능 
            if 0<=nx<=len(park)-1 and 0<=ny<=len(park[0])-1 and park[nx][ny]!='X':
                canmove=True
                xx,yy = nx,ny
            else:
                canmove=False
                break 
                
        if canmove :
            x,y = nx,ny
    
        
    return [x,y]
def solution(triangle):
    answer = triangle[0][0] 
    x,y= 1,1
    # 합이 가장 큰 경우
    
    for i in range(1,len(triangle)) :
        for j in range(i+1):
            # 1번째 값의 경우, 윗줄의 1번째 값 1개만 더함 
            if j==0:
                triangle[i][j] += triangle[i-1][j] 
            # 맨끝 값의 경우, 윗줄의 맨끝 값 1개만 더함
            elif j==i:
                triangle[i][j] += triangle[i-1][j-1] 
            # 중간에 있는 값의 경우, 윗줄의 이전과 이후 값을 더함
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    return max(triangle[-1])  # 계속 더해갈 때 맨 마지막 줄 값 출력 

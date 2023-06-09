# # 완전탐색
# # 옮기면서 돌리면 기존 자물쇠 영역을 삐져나간다 -> lock을 확장시킨다 
# # 시간복잡도: 

# # 2차원 리스트 왼쪽으로 90도 회전
# def rotate90(matrix):
#     n, m = len(matrix), len(matrix[0])  # 행 길이, 열 길이
#     result = [[0]*n for _ in range(m)] 
#     for i in range(n):
#         for j in range(m):
#             result[j][n-i-1] = matrix[i][j]
    
#     return result 


# # 자물쇠 중간부분 모두 1인지 체크
# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length, lock_length*2):
#         for j in range(lock_length, lock_length*2):
#             if new_lock[i][j] != 1:
#                 return False
#     return True 


# def solution(key, lock):
#     answer = True
    
#     n, m = len(key), len(lock)
    
#     # lock 크기 확장
#     new_lock = [[0]*(n*3) for _ in range(n*3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[n+i][n+j] = lock[i][j] # 가운데에 기존 lock 넣기 
    
#     # 4가지 방향에 대해 확인 
#     for rotation in range(4):
#         key = rotate90(key)  #열쇠회전
#         for x in range(n*2):
#             for y in range(n*2):
#                 # 자물쇠에 열쇠 끼기
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사 
#                 if check(new_lock) == True:
#                     return True 
#                 # 자물쇠에서 열쇠 다시 빼기 
#                 for i in range(n):
#                     for j in range(m):
#                         new_lock[x+i][y+j] -= key[i][j]
                     
#     return False



def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False;
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if(check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)
                
    return False
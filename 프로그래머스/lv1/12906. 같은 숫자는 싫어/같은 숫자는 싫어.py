# 연속이면 제거, 순서 유지

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for idx in range(1, len(arr)):
        if arr[idx] != arr[idx-1]:
            answer.append(arr[idx])
        elif arr[idx] == arr[idx-1]:
            pass
    return answer
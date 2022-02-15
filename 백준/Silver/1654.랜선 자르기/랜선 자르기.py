import sys

k, n = map(int, sys.stdin.readline().split()) 
line = []

for _ in range(k):
    line.append(int(sys.stdin.readline()))
start = 1
end = max(line)

# binary search (이진 탐색)
while(start<=end):
    mid = (start+end)//2
    count = 0
    for i in line:
        count += i//mid
    if count >= n:  #자른 개수가 많으면 -> 더 크게잘라야함
        start = mid+1
    else:
        end = mid-1

print(end) 


## [설명] 숫자 up/down 게임을 떠올리면 이해하기 쉽다.
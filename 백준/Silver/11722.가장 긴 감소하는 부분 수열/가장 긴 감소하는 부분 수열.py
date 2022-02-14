n = int(input())  # 입력받은 숫자 개수
A = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
def solution(k, dungeons):
    n = len(dungeons)
    dungeons.sort(key=lambda x: (x[0]-x[1]))

    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for r in range(1, k+1):
            if dungeons[i-1][0] > r:
                dp[i][r] = dp[i-1][r]
            else:
                dp[i][r] = max(dp[i-1][r], 1 + dp[i-1][r-dungeons[i-1][1]])

    return dp[n][k]
def solution(triangle):
    df = [[0 for j in i]for i in triangle]
    df[0][0] = triangle[0][0]

    for i in range(len(triangle)):
        for j in range(i):
            df[i][j] = max(df[i][j], df[i-1][j] + triangle[i][j])
            df[i][j+1] = df[i-1][j] + triangle[i][j+1]
    return max(df[-1])
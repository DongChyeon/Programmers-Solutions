def solution(matrix_sizes):
    INF = int(10e9)
    
    n = len(matrix_sizes) + 1
    d = [matrix_sizes[0][0]]
    for matrix in matrix_sizes:
        d.append(matrix[1])
    
    dp = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        dp[i][i] = 0
        
    for diagonal in range(1, n):
        for i in range(1, n - diagonal):
            j = i + diagonal
            
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], 
                               dp[i][k] + dp[k + 1][j] + (d[i - 1] * d[k] * d[j]))
    
    return dp[1][n - 1]

ef solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    # 물에 잠긴 지역을 -1로 표시
    for puddle in puddles:
        x, y = puddle
        dp[y - 1][x - 1] = -1
    
    # 학교로 가는 길이 없을 경우 0 리턴
    if dp[0][1] == -1 and dp[1][0] == -1:
        return 0
    
    dp[0][0] = 1
    for y in range(n):
        for x in range(m):
            # 물에 잠긴 지역은 계산에 영향을 못 미치도록 0으로 처리
            if dp[y][x] == -1:
                dp[y][x] = 0
            else:
                if x > 0 and y > 0:
                    dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1000000007
                # 가장 위쪽 또는 가장 오른쪽일 경우 예외 처리
                elif x > 0 and y <= 0:
                    dp[y][x] = dp[y][x - 1] % 1000000007
                elif x <= 0 and y > 0:
                    dp[y][x] = dp[y - 1][x] % 1000000007
    
    return dp[n - 1][m - 1]
  

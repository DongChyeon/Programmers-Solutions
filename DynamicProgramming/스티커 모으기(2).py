def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    answer = 0
    dp = [0] * len(sticker)

    # 첫 번째 스티커를 떼고 진행
    dp[0], dp[1] = sticker[0], sticker[0]
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer = dp[-2]
    
    # 첫 번째 스티커를 떼지 않고 진행
    dp[0], dp[1] = 0, sticker[1]
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer = max(answer, dp[-1])
        
    return answer

class Solution {
    fun solution(n: Int): Long {
        val dp = LongArray(2001)
        dp[0] = 0L; dp[1] = 1L; dp[2] = 2L
        for (i in 3..n) dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        
        return dp[n]
    }
}

class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i * i for i in range(1, Math.sqrt(n))]
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in nums:
            for j in range(i, n + 1):
                dp[j] = min(dp[j - i] + 1, dp[j])
        return dp[-1] if dp[-1] != inf else -1

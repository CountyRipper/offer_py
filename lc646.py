class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

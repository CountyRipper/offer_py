class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                # i= n-1时直接跳过
                if s[i] == s[j]:
                    # 当两字符相等，并且i不等于j，新+2回文
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # 不相等时，继承右侧+1或者左侧-1的dp值，实际为dp的正左侧或者正下方的值
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # 最后的dp[0][-1]是 s[0-n]遍历后的最长回文子串值
        return dp[0][-1]

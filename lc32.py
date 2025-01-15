class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    if i > 1:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                    continue
                if i > 1:
                    if s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
            else:
                dp[i] = dp[i - 1]

        return dp[-1]

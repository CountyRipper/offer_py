class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = list(set(wordDict))
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # 从前往后，每一次判定子串是否在word字典里
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break

        return dp[len(s)]

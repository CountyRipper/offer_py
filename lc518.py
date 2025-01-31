class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 完全背包 特定和问题的数量问题，升序遍历，注意边界为1
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] = dp[j] + dp[j - i]
        return dp[-1]

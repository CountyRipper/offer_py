class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)

        dp[0] = 0
        # 完全背包，外层循环价值list，内层循环背包列表
        for i in coins:
            for j in range(i, amount + 1):
                # 选了i硬币和不选i硬币，哪个更小
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[amount] if dp[amount] < inf else -1

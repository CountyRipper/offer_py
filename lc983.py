class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)
        j = 0
        k = 0
        for i, d in enumerate(days):
            while days[j] <= d - 7:
                j += 1
            while (
                days[k] <= d - 30
            ):  # 看的是k指针下一个days是否间隔了30天以上，如果30天以上，那么跳转到下一个days之后一定大于当前d-30
                k += 1
            dp[i + 1] = min(dp[i] + costs[0], dp[j] + costs[1], dp[k] + costs[2])
        return dp[-1]

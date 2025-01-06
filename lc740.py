class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pos = [0] * (max(nums) + 1)
        dp = [0] * len(pos)
        for i in nums:
            pos[i] += 1
        dp[0] = 0
        dp[1] = 1 * pos[1]
        for i in range(2, len(pos)):
            dp[i] = max(dp[i - 1], dp[i - 2] + pos[i] * i)
        return dp[-1]

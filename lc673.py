class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 我们使用双重循环，且仅考虑 nums[i] > nums[j]的情况
        # 如果 dp[j]+1 > dp[i] 这时候说明最长递增子序列应当更新，dp[i]更新
        # 同时也说明这是新记录的长度,count[i] = count[j]
        # 如果dp[j]+1 == dp[i]说明这不是第一次找到这个组合， count[i] += count[j]
        # 最后的结果应该是 max(dp) * max_idx的数量
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        # i应该从1开始，0开始没有意义
        for i in range(1, n):
            for j in range(i):
                # 下面的循环对于dp而言等价于:
                # if nums[i]>nums[j]:
                #   dp[i] = max(dp[i],dp[j]+1)
                if nums[i] > nums[j]:  # 仅考虑这种情况
                    if dp[j] + 1 > dp[i]:  # 第一次出现
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:  # 第一次出现
                        count[i] += count[j]

        max_num = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == max_num:
                res += count[i]
        return res

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = [0] * len(nums)
        m[0] = nums[0]
        if len(nums) > 1:
            m[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            m[i] = max(m[i - 2] + nums[i], m[i - 1])

        return max(m)

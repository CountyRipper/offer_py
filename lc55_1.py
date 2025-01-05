class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_step = nums[0]
        for i in range(len(nums)):
            if max_step >= len(nums):
                return True
            if i > max_step:
                return False
            else:
                if max_step < (nums[i] + i):
                    max_step = nums[i] + i
        return max_step >= len(nums) - 1

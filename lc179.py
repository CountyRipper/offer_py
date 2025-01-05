class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        res = ""
        sorted(nums, reverse=True)
        for i in nums:
            res += i
        return res

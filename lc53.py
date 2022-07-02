from typing import List
#动态规划，在i点上f(i) = max(f(i-1)+nums[i],nums[i])
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #l,r = 0,0
        res = nums[0]
        f = res
        for i in range(1,len(nums)):
            f = max(f+nums[i],nums[i])
            res = max(f,res)
        return res
s1 = Solution()
list = [5,4,-1,7,8]
print(s1.maxSubArray(list))
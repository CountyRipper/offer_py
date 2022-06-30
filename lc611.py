from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)<3): return 0
        sum = 0
        for i in range(len(nums)):
            k=i
            for j in range(i+1,len(nums)):
                while k+1<len(nums) and nums[i]+nums[j]>nums[k+1]:
                    k=k+1
                sum+=max(k-j,0)
        return sum
s1= Solution()
list = [2,2,3,4]
print(s1.triangleNumber(list))
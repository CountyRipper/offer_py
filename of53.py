from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums)<2:
            if nums[0]==0:
                return 1
            else: return 0
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r+1)//2
            if nums[mid]==mid:
                l=mid
            else:
                r=mid-1
        if nums[l]!=l:
            return l
        else:
            return l+1
S1= Solution()
list=[0,1,3]
print(S1.missingNumber(list))
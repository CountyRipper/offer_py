from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<right:
            mid = (right-left)//2+left
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            else:
                left=mid+1
        if nums[left]<target:
            return left+1
        if nums[right]>target:
            return right
        return left
s = Solution()
list = [1,3]
target = 0
print(s.searchInsert(list,target))
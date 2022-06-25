from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #res=[-1,-1]
        if len(nums)<=0 or nums[0]>target or nums[-1]<target:
            return [-1,-1]
        l = bindivl(nums,target)
        r = bindivr(nums,target)
        if l<=r and r < len(nums) and nums[l]==target and nums[r]==target:
            return [l,r]
        else:
            return [-1,-1]
        
        
def bindivl(nums: List[int], target: int):
    left,right=0,len(nums)-1
    while left<right:
        mid = (left+right)//2
        if nums[mid]>=target:
            right = mid
        else:
            left = mid+1
    return left  
def bindivr(nums: List[int], target: int):
    left,right=0,len(nums)-1
    while left<right:
        mid = (left+right+1)//2
        if nums[mid]<=target:
            left = mid
        else:
            right = mid-1
    return left                 
s = Solution()
list = [5,7,7,8,8,10]
target = 8
print(s.searchRange(list,target))
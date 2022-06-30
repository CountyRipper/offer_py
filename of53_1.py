from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binserl
        '''
        if len(nums)==0: return 0
        if len(nums)==1:
            if target==nums[0]:
                 return 1
            else: return 0
        l1,r1=0,len(nums)-1
        while l1<r1:
            mid1 = (l1+r1)//2
            if target<=nums[mid1]:
                r1 = mid1
            else:
                l1=mid1+1
        l2,r2=0,len(nums)-1
        while l2<r2:
            mid2=(l2+r2+1)//2
            if target>=nums[mid2]:
                l2=mid2
            else:
                r2=mid2-1
        if nums[l1]==target:
            return l2-l1+1
        else:
            return 0
s1 = Solution()
list = [2,2]
target = 1
print(s1.search(list,target))
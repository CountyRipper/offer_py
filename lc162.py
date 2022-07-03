from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(i: int) -> int:
            if i == -1:
                return float('-inf')
            else:
                return nums[i]
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r+1)//2
            if get(mid) >= get(mid-1) and get(mid) >= get(mid+1):
                return mid
            elif get(mid) < get(mid-1):
                r = mid-1
            elif get(mid) < get(mid+1):
                l = mid
        return l

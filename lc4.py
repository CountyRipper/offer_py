from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1+nums2
        s.sort()
        if len(s)%2==0:
            return (s[(len(s)-1)/2]+s[len(s)/2])/2 
        else:
            return s[len(s)//2]
            
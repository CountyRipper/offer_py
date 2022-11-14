
from functools import partial
from typing import List
def parition(nums: List[int],l:int,r:int,k:int):
    i,j=l,r
    pivot = nums[l]
    while i<j:
        while i<j and nums[j]>=pivot: j=j-1
        while i<j and nums[i]<pivot: i=i+1
        
        nums[i],nums[j] = nums[j], nums[i]
    nums[l],nums[i] = nums[i],nums[l]    
    if i>k :
        #在左侧
        return parition(nums,l,i-1,k)
    elif i<k:
        #在右侧
        return parition(nums,i+1,r,k)
    else: return  nums[i]
def findKthLargest( nums: List[int], k: int) -> int:    
    return parition(nums,0,len(nums)-1,k-1)
    
list = [3,2,1,5,6,4]
print(findKthLargest(list,2))    
    
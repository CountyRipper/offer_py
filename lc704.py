from typing import List
def search( nums: List[int], target: int) -> int:
    start = 0
    end= len(nums)-1
    while start<=end:
        mid=(end+start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1
       
l = [-1,0,3,5,9,12]
print(search(l,9))
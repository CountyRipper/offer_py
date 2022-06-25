from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = nums[0]
        for i in range(len(nums)-1):
            if i+1>a :
                return False
            else:
                if nums[i+1]+i+1>a:
                    a=nums[i+1]+i+1
        return True
s1 =Solution()
ml = [1,1,1,0]
print(s1.canJump(ml))
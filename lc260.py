from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        sum = 0
        for i in nums:
            sum^=i
        #核心算法在于 x&-x 可以取到最低位1的数
        f = sum&(-sum)
        t1,t2=0,0
        for i in nums:
            if i&f:
                t1^=i
            else:
                t2^=i
        return [t1,t2]
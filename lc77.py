from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1,n+1)
        size = len(nums)
        res=[]
        def backtrack(start,path: List[int]):
            if len(path)==k:
                res.append(path.copy())
                return
            for i in range(start,size+1):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return res
    
                
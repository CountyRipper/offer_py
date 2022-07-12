from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        nums= [1,2,3,4,5,6,7,8,9]
        def trackback(index,path,m):  
            if m==k:
                if sum(path)==n:
                    res.append(path.copy())           
            if m>k:
                return
            for i in range(index,9):
                path.append(nums[i])
                trackback(i+1,path,m+1)
                path.pop()
        trackback(0,[],0)
        return res
s1=Solution()
print(s1.combinationSum3(3,7))
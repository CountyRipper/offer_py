from typing import List
class Solution:         
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def backtrack(i,path: List[int]):
            res.append(path)
            #把当前的分支加入
            for j in range(i,n):
                path.append(nums[j])#做出选择
                backtrack(j+1,path)
                path.pop() #撤销上次的选择
        backtrack(0,[])
        return res

s1 =Solution()
list=[1,2]
print(s1.subsets(list))
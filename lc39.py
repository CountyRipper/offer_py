from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res=[]
        candidates.sort()
        def backtarck(start,path: List[int],residue):
            if residue==0:
                res.append(path.copy())
                return
            for i in range(start,n):
                if residue<candidates[i]:
                    break
                path.append(candidates[i])
                #可重复利用的核心在于i而不是i+1
                backtarck(i,path,residue-candidates[i])
                path.pop()
        backtarck(0,[],target)
        return res
s1 = Solution()
list=[2,3,6,7]
target=7
print(s1.combinationSum(list,target))   
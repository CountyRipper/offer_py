from calendar import c
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        tmp=[]
        def trackback(start,choose :List[int],residue):
            if residue==0:
                tmp.append(choose.copy())
                return
            for i in range(start,n):
                #剪枝
                if candidates[i]>residue:
                    break
                #配合排序去重
                if i>start and candidates[i-1]==candidates[i]:
                    continue
                
                choose.append(candidates[i])
                trackback(i+1,choose,residue-candidates[i])                     
                choose.pop()
        if n ==0:
            return []
        candidates.sort()
        trackback(0,[],target)
        return tmp 
s1 = Solution()
list=[2,5,2,1,2]
target=5
print(s1.combinationSum2(list,target))                 
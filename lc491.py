from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
    path=[]
    res=[]
    def DFS(numss):
        tmp=set()
        #cur<n
        for i,val in enumerate(numss):
            if val not in tmp and (not path or val >= path[-1]):
                tmp.add(val)
                path.append(val)
                DFS(numss[i+1:])
                path.pop()
        if len(path)>=2:
            res.append(path.copy())
    DFS(nums)
    return res
nums = [4,6,7,7]
print(findSubsequences(nums))
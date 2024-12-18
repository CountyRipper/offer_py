from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
        res = []
        path=[]
        def DFS(path,i):
            if len(path)>4: return
            if len(path)==4:
                if sum(path)==target and path not in res: res.append(path.copy())
                else: return
            else:
                for j in range(i,len(nums)):
                    path.append(nums[j])
                    DFS(path,j+1)
                    path.pop()
        DFS(path,0)
        return res
print(fourSum([1,0,-1,0,-2,2],0))
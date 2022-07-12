from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def trackback(index,path: List[int],depth):
            if depth==n:
                res.append(path.copy())
                return
            for i in range(n):
                if (index>>i)&1==0:
                    #说明目前还没有装填完毕
                    path.append(nums[i])
                    #把添加进去的那一位置为0
                    trackback(index^(1<<i),path,depth+1)
                    path.pop()
        trackback(0,[],0)
        return res
s1=Solution()
list=[1,3,5]
print(s1.permute(list))

            
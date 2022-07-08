import collections
from inspect import _void
from typing import List
from typing_extensions import Self
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        res=0
        nr,nc=len(grid),len(grid[0])
        Q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    res+=1
                    Q.append([i,j])
                    while Q:
                        r,c = Q.popleft()
                        #取得头部元素
                        for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                            if 0<=x<nr and 0<=y<nc and grid[x][y]=='1':
                                grid[x][y]=0
                                Q.append([x,y])
        return res
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s1 = Solution()
print(s1.numIslands(grid))
                
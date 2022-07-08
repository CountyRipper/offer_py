from inspect import _void
from typing import List
from typing_extensions import Self
class Solution:
    def dfs(self,grid, i,j):
        grid[i][j]=0
        nr,nc=len(grid),len(grid[0])
        for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
            if 0<=x<nr and 0<=y<nc and grid[x][y]=='1':
                self.dfs(grid,x,y)
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    res+=1
        return res
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s1 = Solution()
print(s1.numIslands(grid))
                
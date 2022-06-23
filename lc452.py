from ast import List
from pip import main
from typing import List

class Solution(object):
    def findMinArrowShots(self, points: List[List[int]]) -> int:    # type: ignore
        if not points:
            return 0
        points.sort(key= lambda x:x[1])  
        end = points[0][1]  
        res = 1
        for x in points:  
            if x[0] >end:
                end = x[1]
                res+=1
        return res   
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
s1 = Solution()
print(s1.findMinArrowShots(points))
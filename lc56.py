from turtle import left
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        res=[]
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=right:
                if intervals[i][1]>right:
                    right=intervals[i][1]
            else:
                #大于，更新结果
                res.append([left,right])
                left=intervals[i][0]
                right=intervals[i][1]
        res.append([left,right])
        return res
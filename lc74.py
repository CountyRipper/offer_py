from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0, len(matrix)-1
        mid1=0
        while top<bottom :
            mid1 = (top+bottom+1)//2
            if target > matrix[mid1][-1]:
                top = mid1
            elif target < matrix[mid1][0]:
                bottom = mid1-1
            else:
                break
        if top!=bottom:
            row=mid1
        else:
            row=top
        if matrix[row][-1]<target or matrix[row][0]>target:
            return False
        else:
            l,r = 0, len(matrix[row])-1
            while l<r:
                mid2 = (l+r+1)//2
                if matrix[row][mid2]>target:
                    r = mid2-1
                elif matrix[row][mid2]<target:
                    l=mid2
                else:
                    return True
            if matrix[row][l]!=target:
                return False
            else: return True
s1 = Solution()
list = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(s1.searchMatrix(list,target))         
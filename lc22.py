from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur=''
        def backtrack(left,right,cur: str):
            if left==n and right==n:
                res.append(cur)
            if left<right:
                return   #用于限制括号合理性
            if left<n:
                backtrack(left+1,right,cur+'(')
            if right<n:
                backtrack(left,right+1,cur+')')
        backtrack(0,0,cur)
        return res
                
        
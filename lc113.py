from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        path=[]
        def DFS(root: Optional[TreeNode],path):
            if not root:
                return 
            if sum(path)==targetSum and not root.left and not root.right:
                res.append(path.copy())
            path.append(root.val)
            if root.left:
                DFS(root.left,path)
            if root.right:
                DFS(root.right,path)
            path.pop()
        DFS(root,path)
        return res
s1=Solution()

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        tmp=root
        s=[]
        while tmp or len(s)>0:
            if tmp.left:
                s.append(tmp)
                tmp=tmp.left
            else:
                tmp=s[-1]
                s.pop()
                res.append(tmp.val)
                tmp=tmp.right
        return res
        
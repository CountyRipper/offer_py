# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res= 0
        if not root:
            return res
        curq=[]
        cur = root
        curq.append(cur)
        while curq:
            res+=1
            n =len(curq)
            for i in range(n):
                if curq[i].left:
                    curq.append(curq[i].left)
                if curq[i].right:
                    curq.append(curq[i].right)
            for i in range(n):
                curq.remove()
        return res
            
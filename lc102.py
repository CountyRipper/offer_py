# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root:
            return res
        q1 = []
        q1.append(root)

        while q1:
            path=[]
            for i in q1:
                path.append(i.val)
            n = len(q1)
            for i in range(n):
                if q1[i].left:
                    q1.append(q1[i].left)
                if q1[i].right:
                    q1.append(q1[i].right)
            for i in range(n):
                q1.pop(0)
            res.append(path)
        return res
            
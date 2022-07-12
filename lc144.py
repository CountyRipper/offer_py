from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []
        s = []
        tmp=root
        while tmp or s:
            while tmp:
                res.append(tmp.val)
                s.append(tmp)
                tmp=tmp.left
            #进入右子树
            if len(s)>0:
                tmp=s[-1]
                s.pop()
                tmp=tmp.right
        return res
                
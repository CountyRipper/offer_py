# Definition for a binary tree node.
from typing  import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1=[] #用于存储先序遍历
        s2=[]
        res=[]
        while root or len(s1)>0:
            if(root):
                s1.append(root)
                s2.append(root)
                root=root.right#注意 root right left顺序
            else:
                root=s1[-1]
                s1.pop()
                root=root.left
        while len(s2)>0:
            res.append(s2.pop().val)
        return res
        
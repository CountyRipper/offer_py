# Definition for a binary tree node.
from typing import List 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def mybuildtree(preorder: List[int], inorder: List[int]):
            if len(preorder)==0:
                return 
            n = len(preorder)
            rootnvalue = preorder[0]
            rootnum =0
            #得到indorder根的位置
            while inorder[rootnum]!=rootnvalue:
                rootnum=rootnum+1
            left_len = rootnum-0
            #right_len = n-1-rootnum
            root = TreeNode(rootnvalue)
            #前闭后开
            root.left=mybuildtree(preorder[1:left_len+1],inorder[:rootnum])
            root.right = mybuildtree(preorder[left_len+1:],inorder[left_len+1:])
            return root
        return mybuildtree(preorder,inorder)
s1 =Solution()
pre=[3,9,20,15,7]
ino = [9,3,15,20,7]
t1 = s1.buildTree(pre,ino)
print(t1)
print("end")

            
        

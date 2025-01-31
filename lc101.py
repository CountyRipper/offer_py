# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left_root: Optional[TreeNode], right_root: Optional[TreeNode]):
            if left_root == None or right_root == None:
                return (
                    left_root is right_root
                )  #    对称：两个都为None，单个为None直接返回False
            # 1.左右两个值相等，2.递归各自的左右对称节点也相等
            return (
                left_root.val == right_root.val
                and dfs(left_root.left, right_root.right)
                and dfs(left_root.right, right_root.left)
            )

        return dfs(root.left, root.right)

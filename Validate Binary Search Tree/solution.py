from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursion(self, root: Optional[TreeNode], in_order_traversal: List[int]):
        if root:
            self.recursion(root.left, in_order_traversal)
            in_order_traversal.append(root.val)
            self.recursion(root.right, in_order_traversal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        in_order_traversal = []
        self.recursion(root, in_order_traversal)

        for i in range(1, len(in_order_traversal)):
            if in_order_traversal[i - 1] >= in_order_traversal[i]:
                return False
        
        return True
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recursion(self, root: Optional[TreeNode], nodes: List[int]):
        if root:
            self.recursion(root.left, nodes)
            nodes.append(root.val)
            self.recursion(root.right, nodes)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        nodes = []
        self.recursion(root, nodes)
        
        return nodes
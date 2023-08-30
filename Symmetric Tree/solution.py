# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def left_helper(self, root: Optional[TreeNode], traversal, tag) -> None:
        if root:
            self.left_helper(root.left, traversal, tag="l")
            traversal.append(str(root.val) + tag)
            self.left_helper(root.right, traversal, tag="r")

    def right_helper(self, root: Optional[TreeNode], traversal, tag) -> None:
        if root:
            self.right_helper(root.right, traversal, tag="l")
            # print("droit ", root.val)
            traversal.append(str(root.val) + tag)
            self.right_helper(root.left, traversal, tag="r")

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_traversal = []
        right_traversal = []

        self.left_helper(root.left, left_traversal, "t")
        self.right_helper(root.right, right_traversal, "t")

        # print(left_traversal)
        # print(right_traversal)

        if len(left_traversal) != len(right_traversal):
            return False

        for i in range(len(left_traversal)):
            if left_traversal[i] != right_traversal[i]:
                return False

        return True

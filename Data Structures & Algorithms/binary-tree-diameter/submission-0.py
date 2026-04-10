# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0

        def getH(node):
            if not node:
                return 0
            
            leftH = getH(node.left)
            rightH = getH(node.right)

            self.maxD = max(self.maxD, leftH + rightH)

            return 1 + max(leftH, rightH)

        getH(root)
        return self.maxD

        
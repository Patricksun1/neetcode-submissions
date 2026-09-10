# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        size = self.treeSize(root)
        if size == 0:
            return None
        if size == 1:
            return root.val
        
        if k <= self.treeSize(root.left):
            return self.kthSmallest(root.left, k)

        elif k > self.treeSize(root.left) + 1:

            return self.kthSmallest(root.right, (k - self.treeSize(root.left) - 1))
        else:
            return root.val



    def treeSize(self, root):
        if root == None:
            return 0
        
        return 1 + self.treeSize(root.left) + self.treeSize(root.right)
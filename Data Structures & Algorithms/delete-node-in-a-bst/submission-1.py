# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            child1 = root.left
            child2 = root.right
            if child1 is None and child2 is None:
                return None
            elif child1 is None:
                return child2
            elif child2 is None:
                return child1
            else:
                curr = child2
                while curr.left:
                    curr = curr.left

            root.val = curr.val
            
            root.right = self.deleteNode(root.right, root.val)

        

    

        return root
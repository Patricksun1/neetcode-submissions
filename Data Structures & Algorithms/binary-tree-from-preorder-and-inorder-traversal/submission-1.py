# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map each value to its inorder index for instant O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. A pointer to track our current root in the preorder array
        self.pre_idx = 0
        
        # 3. Helper function that uses boundaries instead of sliced arrays
        def array_to_tree(left, right):
            # Base case: if left bound passes right bound, the subtree is empty
            if left > right:
                return None
            
            # Fetch the current root value and build the node
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Move our preorder pointer to the next node
            self.pre_idx += 1
            
            # Instantly find where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build subtrees using the new boundaries
            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            
            return root
            
        # Start the recursion spanning the entire inorder array
        return array_to_tree(0, len(inorder) - 1)

      


        
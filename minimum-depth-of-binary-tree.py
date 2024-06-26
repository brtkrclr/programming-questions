# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        Note: A leaf is a node with no children.

        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: 2

        Example 2:
        Input: root = [2,null,3,null,4,null,5,null,6]
        Output: 5
        '''
        if root is None:
            return 0
        elif root.left is None or root.right is None:
            return max(self.minDepth(root.left),self.minDepth(root.right))+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(treeroot):
            if treeroot is None:
                return None
            invert(treeroot.left)
            invert(treeroot.right)
            temp = treeroot.left
            treeroot.left = treeroot.right
            treeroot.right = temp
            return treeroot

        if root == None:
            return None
        return invert(root)
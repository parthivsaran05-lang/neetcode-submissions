# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val=[]
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            val.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(1,len(val)):
            if val[i]<=val[i-1]:
                return False
        return True
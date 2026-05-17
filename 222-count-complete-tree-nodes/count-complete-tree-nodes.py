class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # Count the current node (1) + all left nodes + all right nodes
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
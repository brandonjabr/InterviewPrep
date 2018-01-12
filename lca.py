def lca(root, p, q):
    if root in (None, p, q):
        return root
    left, right = [lca(child, p, q) for child in (root.left, root.right)]
    
    return root if left and right else left or right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

r = TreeNode(3)
r.right = TreeNode(4)
r.left = TreeNode(2)

print(lca(r,r.right,r.left).val)


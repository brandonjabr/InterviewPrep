class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    node_depths = []
    depths = set()
    def addNode(node, depth):
        if not node:
            return
        
        depths.add(depth)
        node_depths.append((node.val,depth))
        
        addNode(node.left,depth+1)
        addNode(node.right,depth+1)
    
    addNode(root, 0)
    
    zigZag = [[] for i in range(len(depths))]
    
    for node in node_depths:
        zigZag[node[1]].append(node[0])
        
    for i in range(1, len(zigZag),2):
        zigZag[i] = zigZag[i][::-1]

    return zigZag

r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15)
r.right.right = TreeNode(7)

print zigzagLevelOrder(r)


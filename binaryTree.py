class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def isSuperbalanced(root):
    nodes = []
    depths = []

    nodes.append((root,0))

    while len(nodes) > 0:

        node, depth = nodes.pop()

        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)

            if len(depths) > 2 or (len(depths) == 2 and abs(depths[1] - depths[0]) >= 2):
                return False
        else:
            if node.left:
                nodes.append((node.left,depth+1))
            if node.right:
                nodes.append((node.right,depth+1))
    return True
            
def is_valid(root):
    nodes = [(root,-float('inf'), float('inf'))]

    while nodes:
        node, lower, upper = nodes.pop()

        if (node.value <= lower) or (node.value >= upper):
            return False
        
        if node.left:
            nodes.append((node.left, lower, node.value))
        if node.right:
            nodes.append((node.right, node.value, upper))
    
    return True

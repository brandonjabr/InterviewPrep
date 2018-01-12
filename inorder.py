def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    elif not root.left and not root.right:
        return root
    
    inorder = []
    
    stack = []
    curr = root
    finished = False
    while not finished:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            if stack:
                curr = stack.pop()
                inorder.append(curr.val)
                curr = curr.right
            else:
                finished = True
    
    return inorder
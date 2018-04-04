def isBST(root):
    return isBST1(root, -1 << 31, 1<<31)


def isBST1(root, min, max):
    if root is None:
        return True
    if min < root.val < max:
        return isBST1(root.left, min, root.val) and isBST1(root.right, root.val, max)
    else:
        return False

pre = None
def isBST2(root):
    global pre
    if root is None:
        return True
    if isBST2(root.left):
        if root.val > pre:
            pre = root.val
            return isBST2(root)
        else:
            return False
    else:
        return False

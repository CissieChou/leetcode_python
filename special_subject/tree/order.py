def preOrder(root):
    if root is None:
        return []
    result = []
    stack = []
    cur = root
    while len(stack) > 0 or cur:
        if cur:
            result.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right

    return result

def inOrder(root):
    if root is None:
        return []
    result = []
    stack = []
    cur = root
    while len(stack) > 0 or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

    return result


def postOrder(root):
    if root is None:
        return []
    result = []
    stack = []
    cur = root
    while len(stack) > 0 or cur:
        if cur:
            stack.append(cur)
            result.insert(0, cur.val)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left

    return result
